"""
Módulo principal da biblioteca Enigma.
Implementa criptografia usando matrizes de permutação e álgebra linear.
"""

import numpy as np
from typing import Tuple, List


def char_to_one_hot(char: str, alphabet: str) -> np.ndarray:
    """
    Converte um caractere em um vetor one-hot.
    
    Um vetor one-hot é uma matriz-coluna onde todos os elementos são zero,
    exceto o elemento correspondente ao caractere no alfabeto, que é 1.
    
    Args:
        char: Caractere a ser convertido
        alphabet: String contendo o alfabeto ordenado
        
    Returns:
        Matriz numpy de shape (len(alphabet), 1) representando o vetor one-hot
        
    Raises:
        ValueError: Se o caractere não estiver no alfabeto
        
    Exemplo:
        >>> alfabeto = "abc"
        >>> char_to_one_hot('a', alfabeto)
        array([[1],
               [0],
               [0]])
    """
    if char not in alphabet:
        raise ValueError(f"Caractere '{char}' não está no alfabeto")
    
    idx = alphabet.index(char)
    one_hot = np.zeros((len(alphabet), 1))
    one_hot[idx, 0] = 1
    return one_hot


def message_to_matrix(message: str, alphabet: str) -> np.ndarray:
    """
    Converte uma mensagem em uma matriz onde cada coluna é um vetor one-hot.
    
    A mensagem é representada como uma matriz M ∈ R^(N×T), onde:
    - N é o número de caracteres no alfabeto
    - T é o número de caracteres na mensagem
    
    Args:
        message: String contendo a mensagem
        alphabet: String contendo o alfabeto ordenado
        
    Returns:
        Matriz numpy de shape (len(alphabet), len(message))
        
    Exemplo:
        >>> alfabeto = "abc"
        >>> message_to_matrix("aabbcc", alfabeto)
        array([[1., 1., 0., 0., 0., 0.],
               [0., 0., 1., 1., 0., 0.],
               [0., 0., 0., 0., 1., 1.]])
    """
    if not message:
        return np.zeros((len(alphabet), 0))
    
    # Verifica se todos os caracteres estão no alfabeto
    for char in message:
        if char not in alphabet:
            raise ValueError(f"Caractere '{char}' não está no alfabeto")
    
    # Cria a matriz coluna por coluna
    columns = [char_to_one_hot(char, alphabet) for char in message]
    return np.hstack(columns)


def alphabet_to_permutation_matrix(alphabet_normal: str, alphabet_cifrado: str) -> np.ndarray:
    """
    Cria uma matriz de permutação P a partir de dois alfabetos.
    
    A matriz P é tal que P * M = M_c, onde M é a mensagem original
    e M_c é a mensagem cifrada.
    
    A matriz de permutação é construída mapeando cada caractere do
    alfabeto normal para sua posição correspondente no alfabeto cifrado.
    
    Args:
        alphabet_normal: Alfabeto original ordenado
        alphabet_cifrado: Alfabeto cifrado (permutação do alfabeto normal)
        
    Returns:
        Matriz numpy de permutação de shape (len(alphabet_normal), len(alphabet_normal))
        
    Raises:
        ValueError: Se os alfabetos não tiverem o mesmo tamanho ou caracteres
        
    Exemplo:
        >>> normal = "abc"
        >>> cifrado = "bca"
        >>> P = alphabet_to_permutation_matrix(normal, cifrado)
        >>> P @ message_to_matrix("abc", normal)
        array([[0., 0., 1.],
               [1., 0., 0.],
               [0., 1., 0.]])
    """
    if len(alphabet_normal) != len(alphabet_cifrado):
        raise ValueError("Os alfabetos devem ter o mesmo tamanho")
    
    if set(alphabet_normal) != set(alphabet_cifrado):
        raise ValueError("Os alfabetos devem conter os mesmos caracteres")
    
    n = len(alphabet_normal)
    P = np.zeros((n, n))
    
    # Para cada caractere no alfabeto normal, encontra sua posição no alfabeto cifrado
    for i, char in enumerate(alphabet_normal):
        j = alphabet_cifrado.index(char)
        P[j, i] = 1
    
    return P


def permutation_matrix_to_alphabet(P: np.ndarray, alphabet_normal: str) -> str:
    """
    Converte uma matriz de permutação de volta para um alfabeto cifrado.
    
    Args:
        P: Matriz de permutação
        alphabet_normal: Alfabeto original ordenado
        
    Returns:
        String contendo o alfabeto cifrado
        
    Exemplo:
        >>> normal = "abc"
        >>> P = alphabet_to_permutation_matrix(normal, "bca")
        >>> permutation_matrix_to_alphabet(P, normal)
        'bca'
    """
    n = len(alphabet_normal)
    if P.shape != (n, n):
        raise ValueError(f"A matriz deve ter shape ({n}, {n})")
    
    # Encontra a posição do 1 em cada coluna
    alphabet_cifrado = [''] * n
    for j in range(n):
        # Encontra a linha onde está o 1 na coluna j
        i = np.argmax(P[:, j])
        alphabet_cifrado[j] = alphabet_normal[i]
    
    return ''.join(alphabet_cifrado)


def cifrar(mensagem_entrada: str, alphabet_normal: str, alphabet_cifrado: str) -> str:
    """
    Cifra uma mensagem usando substituição simples.
    
    Esta função implementa a cifra de substituição básica, onde cada
    caractere é substituído por seu correspondente no alfabeto cifrado.
    
    Args:
        mensagem_entrada: Mensagem a ser cifrada
        alphabet_normal: Alfabeto original
        alphabet_cifrado: Alfabeto cifrado (permutação do alfabeto normal)
        
    Returns:
        String contendo a mensagem cifrada
        
    Exemplo:
        >>> normal = "abcdefghijklmnopqrstuvwxyz "
        >>> cifrado = "bcdefghijkl mnopqrstuvwxyza"
        >>> cifrar("abc", normal, cifrado)
        'bcd'
    """
    mensagem_cifrada = ""
    for char in mensagem_entrada:
        if char not in alphabet_normal:
            raise ValueError(f"Caractere '{char}' não está no alfabeto normal")
        idx = alphabet_normal.index(char)
        mensagem_cifrada += alphabet_cifrado[idx]
    return mensagem_cifrada


def decifrar(mensagem_cifrada: str, alphabet_cifrado: str, alphabet_normal: str) -> str:
    """
    Decifra uma mensagem usando substituição simples.
    
    Esta é a operação inversa de cifrar. Decifra usando o alfabeto cifrado
    como origem e o alfabeto normal como destino.
    
    Args:
        mensagem_cifrada: Mensagem cifrada
        alphabet_cifrado: Alfabeto cifrado
        alphabet_normal: Alfabeto original
        
    Returns:
        String contendo a mensagem decifrada
    """
    return cifrar(mensagem_cifrada, alphabet_cifrado, alphabet_normal)


def enigma(mensagem_entrada: str, alphabet_normal: str, 
           alphabet_cifrado: str, cifrador_auxiliar: str) -> str:
    """
    Cifra uma mensagem usando a máquina Enigma.
    
    A máquina Enigma funciona aplicando uma cifra de substituição, mas
    a cada caractere cifrado, o alfabeto cifrado é permutado usando o
    cifrador auxiliar. Isso torna a criptografia mais segura, pois a
    mesma letra na mensagem original pode ser cifrada de formas diferentes
    dependendo de sua posição.
    
    Implementação usando álgebra linear:
    1. Para cada caractere, aplica a permutação atual
    2. Após cada caractere, atualiza a permutação aplicando o cifrador auxiliar
    
    Args:
        mensagem_entrada: Mensagem a ser cifrada
        alphabet_normal: Alfabeto original
        alphabet_cifrado: Alfabeto cifrado inicial (permutação do alfabeto normal)
        cifrador_auxiliar: Alfabeto usado para permutar o alfabeto cifrado
        
    Returns:
        String contendo a mensagem cifrada
        
    Exemplo:
        >>> normal = "abcdefghijklmnopqrstuvwxyz "
        >>> cifrado = "bcdefghijkl mnopqrstuvwxyza"
        >>> auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"
        >>> enigma("abc", normal, cifrado, auxiliar)
        'bdf'
    """
    mensagem_cifrada = ""
    alfabeto_cifrado_atual = alphabet_cifrado
    
    for char in mensagem_entrada:
        if char not in alphabet_normal:
            raise ValueError(f"Caractere '{char}' não está no alfabeto normal")
        
        # Cifra o caractere usando o alfabeto cifrado atual
        idx = alphabet_normal.index(char)
        mensagem_cifrada += alfabeto_cifrado_atual[idx]
        
        # Atualiza o alfabeto cifrado aplicando o cifrador auxiliar
        alfabeto_cifrado_atual = cifrar(alfabeto_cifrado_atual, alphabet_normal, cifrador_auxiliar)
    
    return mensagem_cifrada


def enigma_decifrar(mensagem_cifrada: str, alphabet_normal: str,
                    alphabet_cifrado: str, cifrador_auxiliar: str) -> str:
    """
    Decifra uma mensagem cifrada pela máquina Enigma.
    
    Para decifrar, é necessário aplicar o processo inverso:
    1. Para cada caractere cifrado, encontra o caractere original
    2. Antes de processar o próximo caractere, reverte a permutação do alfabeto
    
    Args:
        mensagem_cifrada: Mensagem cifrada
        alphabet_normal: Alfabeto original
        alphabet_cifrado: Alfabeto cifrado inicial (deve ser o mesmo usado na cifra)
        cifrador_auxiliar: Alfabeto auxiliar (deve ser o mesmo usado na cifra)
        
    Returns:
        String contendo a mensagem decifrada
    """
    mensagem_decifrada = ""
    alfabeto_cifrado_atual = alphabet_cifrado
    
    for char in mensagem_cifrada:
        if char not in alfabeto_cifrado_atual:
            raise ValueError(f"Caractere '{char}' não está no alfabeto cifrado")
        
        # Encontra o índice no alfabeto cifrado atual
        idx = alfabeto_cifrado_atual.index(char)
        # Recupera o caractere original do alfabeto normal
        mensagem_decifrada += alphabet_normal[idx]
        
        # Atualiza o alfabeto cifrado (mesma operação da cifra)
        alfabeto_cifrado_atual = cifrar(alfabeto_cifrado_atual, alphabet_normal, cifrador_auxiliar)
    
    return mensagem_decifrada


def enigma_matricial(mensagem_entrada: str, alphabet_normal: str,
                     alphabet_cifrado: str, cifrador_auxiliar: str) -> Tuple[str, List[np.ndarray]]:
    """
    Versão matricial da cifra Enigma.
    
    Esta função implementa a máquina Enigma usando operações matriciais.
    Retorna tanto a mensagem cifrada quanto as matrizes de permutação usadas.
    
    Args:
        mensagem_entrada: Mensagem a ser cifrada
        alphabet_normal: Alfabeto original
        alphabet_cifrado: Alfabeto cifrado inicial
        cifrador_auxiliar: Alfabeto auxiliar para permutar
        
    Returns:
        Tupla contendo:
        - String com a mensagem cifrada
        - Lista de matrizes de permutação usadas para cada caractere
    """
    if not mensagem_entrada:
        return "", []
    
    # Converte a mensagem para matriz
    M = message_to_matrix(mensagem_entrada, alphabet_normal)
    
    # Matriz de permutação inicial
    P_atual = alphabet_to_permutation_matrix(alphabet_normal, alphabet_cifrado)
    P_auxiliar = alphabet_to_permutation_matrix(alphabet_normal, cifrador_auxiliar)
    
    # Cifra caractere por caractere
    mensagem_cifrada = ""
    matrizes_permutacao = []
    alfabeto_cifrado_atual = alphabet_cifrado
    
    for i in range(len(mensagem_entrada)):
        # Aplica a permutação atual ao caractere
        char_vector = M[:, i:i+1]
        char_cifrado_vector = P_atual @ char_vector
        
        # Converte o vetor one-hot de volta para caractere
        idx = np.argmax(char_cifrado_vector)
        char_cifrado = alfabeto_cifrado_atual[idx]
        mensagem_cifrada += char_cifrado
        
        # Armazena a matriz de permutação usada
        matrizes_permutacao.append(P_atual.copy())
        
        # Atualiza o alfabeto cifrado e a matriz de permutação
        alfabeto_cifrado_atual = cifrar(alfabeto_cifrado_atual, alphabet_normal, cifrador_auxiliar)
        P_atual = alphabet_to_permutation_matrix(alphabet_normal, alfabeto_cifrado_atual)
    
    return mensagem_cifrada, matrizes_permutacao

