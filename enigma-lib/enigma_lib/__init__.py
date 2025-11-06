"""
Biblioteca Enigma - Criptografia usando álgebra linear
Implementação de uma máquina Enigma digital usando matrizes de permutação.
"""

from .enigma import (
    char_to_one_hot,
    message_to_matrix,
    alphabet_to_permutation_matrix,
    permutation_matrix_to_alphabet,
    cifrar,
    enigma,
    decifrar,
    enigma_decifrar,
    enigma_matricial
)

__version__ = "0.1.0"
__all__ = [
    "char_to_one_hot",
    "message_to_matrix",
    "alphabet_to_permutation_matrix",
    "permutation_matrix_to_alphabet",
    "cifrar",
    "enigma",
    "decifrar",
    "enigma_decifrar",
    "enigma_matricial"
]

