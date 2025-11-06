"""
Testes para a biblioteca Enigma.
Verifica se todas as funções estão funcionando corretamente.
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


def test_char_to_one_hot():
    """Testa a conversão de caractere para one-hot."""
    alfabeto = "abc"
    vetor_a = char_to_one_hot('a', alfabeto)
    assert vetor_a.shape == (3, 1)
    assert vetor_a[0, 0] == 1
    assert vetor_a[1, 0] == 0
    assert vetor_a[2, 0] == 0
    print("✓ test_char_to_one_hot passou")


def test_message_to_matrix():
    """Testa a conversão de mensagem para matriz."""
    alfabeto = "abc"
    M = message_to_matrix("aabbcc", alfabeto)
    assert M.shape == (3, 6)
    assert np.allclose(M[:, 0], [1, 0, 0])  # 'a'
    assert np.allclose(M[:, 1], [1, 0, 0])  # 'a'
    assert np.allclose(M[:, 2], [0, 1, 0])  # 'b'
    assert np.allclose(M[:, 3], [0, 1, 0])  # 'b'
    assert np.allclose(M[:, 4], [0, 0, 1])  # 'c'
    assert np.allclose(M[:, 5], [0, 0, 1])  # 'c'
    print("✓ test_message_to_matrix passou")


def test_alphabet_to_permutation_matrix():
    """Testa a criação de matriz de permutação."""
    normal = "abc"
    cifrado = "bca"
    P = alphabet_to_permutation_matrix(normal, cifrado)
    assert P.shape == (3, 3)
    # Verifica que é uma matriz de permutação (soma de cada linha e coluna = 1)
    assert np.allclose(P.sum(axis=0), 1)
    assert np.allclose(P.sum(axis=1), 1)
    print("✓ test_alphabet_to_permutation_matrix passou")


def test_permutation_matrix_to_alphabet():
    """Testa a conversão de matriz de permutação para alfabeto."""
    normal = "abc"
    cifrado = "bca"
    P = alphabet_to_permutation_matrix(normal, cifrado)
    alfabeto_recuperado = permutation_matrix_to_alphabet(P, normal)
    assert alfabeto_recuperado == cifrado
    print("✓ test_permutation_matrix_to_alphabet passou")


def test_cifrar_decifrar():
    """Testa cifra e decifra simples."""
    normal = "abc"
    cifrado = "bca"
    mensagem = "abc"
    
    mensagem_cifrada = cifrar(mensagem, normal, cifrado)
    assert mensagem_cifrada == "bca"
    
    mensagem_recuperada = decifrar(mensagem_cifrada, cifrado, normal)
    assert mensagem_recuperada == mensagem
    print("✓ test_cifrar_decifrar passou")


def test_enigma():
    """Testa a máquina Enigma."""
    normal = "abc"
    cifrado = "bca"
    auxiliar = "cab"
    mensagem = "abc"
    
    mensagem_cifrada = enigma(mensagem, normal, cifrado, auxiliar)
    mensagem_recuperada = enigma_decifrar(mensagem_cifrada, normal, cifrado, auxiliar)
    assert mensagem_recuperada == mensagem
    print("✓ test_enigma passou")


def test_enigma_vs_simples():
    """Testa que Enigma cifra diferente de cifra simples."""
    normal = "abc"
    cifrado = "bca"
    auxiliar = "cab"
    mensagem = "aaa"
    
    cifrada_simples = cifrar(mensagem, normal, cifrado)
    cifrada_enigma = enigma(mensagem, normal, cifrado, auxiliar)
    
    # Com Enigma, a mesma letra deve ser cifrada diferente em cada posição
    assert cifrada_simples == "bbb"  # Todas iguais
    assert len(set(cifrada_enigma)) > 1 or cifrada_enigma != "bbb"  # Pelo menos uma diferente
    print("✓ test_enigma_vs_simples passou")


def test_exemplo_projeto():
    """Testa o exemplo do projeto."""
    alfabeto_normal = "abcdefghijklmnopqrstuvwxyz "
    alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
    cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"
    mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"
    
    # Testa Enigma
    mensagem_cifrada = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
    mensagem_recuperada = enigma_decifrar(mensagem_cifrada, alfabeto_normal, 
                                           alfabeto_cifrado, cifrador_auxiliar)
    assert mensagem_recuperada == mensagem
    print("✓ test_exemplo_projeto passou")


def test_enigma_matricial():
    """Testa a versão matricial do Enigma."""
    normal = "abc"
    cifrado = "bca"
    auxiliar = "cab"
    mensagem = "abc"
    
    mensagem_cifrada, matrizes = enigma_matricial(mensagem, normal, cifrado, auxiliar)
    mensagem_cifrada_string = enigma(mensagem, normal, cifrado, auxiliar)
    
    assert mensagem_cifrada == mensagem_cifrada_string
    assert len(matrizes) == len(mensagem)
    print("✓ test_enigma_matricial passou")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TESTES DA BIBLIOTECA ENIGMA")
    print("=" * 60 + "\n")
    
    try:
        test_char_to_one_hot()
        test_message_to_matrix()
        test_alphabet_to_permutation_matrix()
        test_permutation_matrix_to_alphabet()
        test_cifrar_decifrar()
        test_enigma()
        test_enigma_vs_simples()
        test_exemplo_projeto()
        test_enigma_matricial()
        
        print("\n" + "=" * 60)
        print("✓ TODOS OS TESTES PASSARAM!")
        print("=" * 60 + "\n")
    except AssertionError as e:
        print(f"\n✗ TESTE FALHOU: {e}\n")
        raise
    except Exception as e:
        print(f"\n✗ ERRO: {e}\n")
        raise

