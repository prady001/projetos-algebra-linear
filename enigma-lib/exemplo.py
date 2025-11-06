"""
Exemplo de uso da biblioteca Enigma.
Demonstra as funcionalidades principais da biblioteca.
"""

from enigma_lib import (
    cifrar,
    decifrar,
    enigma,
    enigma_decifrar,
    char_to_one_hot,
    message_to_matrix,
    alphabet_to_permutation_matrix,
    permutation_matrix_to_alphabet,
    enigma_matricial
)
import numpy as np


def exemplo_cifra_simples():
    """Exemplo de cifra de substituição simples."""
    print("=" * 60)
    print("Exemplo 1: Cifra de Substituição Simples")
    print("=" * 60)
    
    alfabeto_normal = "abcdefghijklmnopqrstuvwxyz "
    alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
    mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"
    
    print(f"Mensagem original: {mensagem}")
    
    mensagem_cifrada = cifrar(mensagem, alfabeto_normal, alfabeto_cifrado)
    print(f"Mensagem cifrada:   {mensagem_cifrada}")
    
    mensagem_recuperada = decifrar(mensagem_cifrada, alfabeto_cifrado, alfabeto_normal)
    print(f"Mensagem recuperada: {mensagem_recuperada}")
    print(f"✓ Decifragem correta: {mensagem == mensagem_recuperada}\n")


def exemplo_enigma():
    """Exemplo de uso da máquina Enigma."""
    print("=" * 60)
    print("Exemplo 2: Máquina Enigma")
    print("=" * 60)
    
    alfabeto_normal = "abcdefghijklmnopqrstuvwxyz "
    alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
    cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"
    mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"
    
    print(f"Mensagem original: {mensagem}")
    
    mensagem_cifrada = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
    print(f"Mensagem cifrada:   {mensagem_cifrada}")
    
    mensagem_recuperada = enigma_decifrar(mensagem_cifrada, alfabeto_normal, 
                                          alfabeto_cifrado, cifrador_auxiliar)
    print(f"Mensagem recuperada: {mensagem_recuperada}")
    print(f"✓ Decifragem correta: {mensagem == mensagem_recuperada}\n")


def exemplo_one_hot():
    """Exemplo de one-hot encoding."""
    print("=" * 60)
    print("Exemplo 3: One-Hot Encoding")
    print("=" * 60)
    
    alfabeto = "abc"
    
    print(f"Alfabeto: {alfabeto}\n")
    
    for char in alfabeto:
        vetor = char_to_one_hot(char, alfabeto)
        print(f"'{char}' -> {vetor.flatten()}")
    
    print()


def exemplo_matriz_mensagem():
    """Exemplo de conversão de mensagem para matriz."""
    print("=" * 60)
    print("Exemplo 4: Mensagem como Matriz")
    print("=" * 60)
    
    alfabeto = "abc"
    mensagem = "aabbcc"
    
    M = message_to_matrix(mensagem, alfabeto)
    
    print(f"Mensagem: {mensagem}")
    print(f"Alfabeto: {alfabeto}")
    print(f"\nMatriz M (cada coluna é um caractere):")
    print(M)
    print(f"\nDimensões: {M.shape} (N={M.shape[0]} caracteres no alfabeto, T={M.shape[1]} caracteres na mensagem)\n")


def exemplo_permutacao_matricial():
    """Exemplo de permutação usando matrizes."""
    print("=" * 60)
    print("Exemplo 5: Permutação Matricial")
    print("=" * 60)
    
    alfabeto_normal = "abc"
    alfabeto_cifrado = "bca"
    mensagem = "aabbcc"
    
    print(f"Alfabeto normal:   {alfabeto_normal}")
    print(f"Alfabeto cifrado:  {alfabeto_cifrado}")
    print(f"Mensagem original: {mensagem}\n")
    
    # Converte mensagem para matriz
    M = message_to_matrix(mensagem, alfabeto_normal)
    print("Matriz M (mensagem original):")
    print(M)
    print()
    
    # Cria matriz de permutação
    P = alphabet_to_permutation_matrix(alfabeto_normal, alfabeto_cifrado)
    print("Matriz de permutação P:")
    print(P)
    print()
    
    # Aplica permutação
    M_cifrada = P @ M
    print("Matriz M_cifrada = P @ M:")
    print(M_cifrada)
    print()
    
    # Recupera alfabeto da matriz de permutação
    alfabeto_recuperado = permutation_matrix_to_alphabet(P, alfabeto_normal)
    print(f"Alfabeto recuperado de P: {alfabeto_recuperado}")
    print(f"✓ Alfabeto correto: {alfabeto_cifrado == alfabeto_recuperado}\n")


def exemplo_enigma_matricial():
    """Exemplo de Enigma usando operações matriciais."""
    print("=" * 60)
    print("Exemplo 6: Enigma Matricial")
    print("=" * 60)
    
    alfabeto_normal = "abc"
    alfabeto_cifrado = "bca"
    cifrador_auxiliar = "cab"
    mensagem = "abc"
    
    print(f"Alfabeto normal:   {alfabeto_normal}")
    print(f"Alfabeto cifrado:  {alfabeto_cifrado}")
    print(f"Cifrador auxiliar: {cifrador_auxiliar}")
    print(f"Mensagem:          {mensagem}\n")
    
    # Versão matricial
    mensagem_cifrada, matrizes = enigma_matricial(mensagem, alfabeto_normal, 
                                                   alfabeto_cifrado, cifrador_auxiliar)
    
    print(f"Mensagem cifrada: {mensagem_cifrada}")
    print(f"\nNúmero de matrizes de permutação usadas: {len(matrizes)}")
    print("\nMatrizes de permutação usadas:")
    for i, P in enumerate(matrizes):
        print(f"\nCaractere {i+1} ({mensagem[i]}):")
        print(P)
    
    # Compara com versão string
    mensagem_cifrada_string = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
    print(f"\n✓ Resultados coincidem: {mensagem_cifrada == mensagem_cifrada_string}\n")


def exemplo_comparacao():
    """Compara cifra simples vs Enigma."""
    print("=" * 60)
    print("Exemplo 7: Comparação Cifra Simples vs Enigma")
    print("=" * 60)
    
    alfabeto_normal = "abcdefghijklmnopqrstuvwxyz "
    alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
    cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"
    mensagem = "aaa"
    
    print(f"Mensagem: {mensagem}\n")
    
    # Cifra simples
    cifrada_simples = cifrar(mensagem, alfabeto_normal, alfabeto_cifrado)
    print(f"Cifra simples:     {cifrada_simples}")
    print("  (mesma letra sempre cifrada igual)\n")
    
    # Enigma
    cifrada_enigma = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
    print(f"Enigma:           {cifrada_enigma}")
    print("  (mesma letra cifrada diferente em cada posição)\n")
    
    print("✓ A máquina Enigma é mais segura porque a mesma letra")
    print("  é cifrada de forma diferente dependendo da posição!\n")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("BIBLIOTECA ENIGMA - EXEMPLOS DE USO")
    print("=" * 60 + "\n")
    
    exemplo_cifra_simples()
    exemplo_enigma()
    exemplo_one_hot()
    exemplo_matriz_mensagem()
    exemplo_permutacao_matricial()
    exemplo_enigma_matricial()
    exemplo_comparacao()
    
    print("=" * 60)
    print("FIM DOS EXEMPLOS")
    print("=" * 60)

