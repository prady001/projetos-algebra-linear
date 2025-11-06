# Biblioteca Enigma

Biblioteca Python para criptografia usando uma implementação digital da máquina Enigma, baseada em álgebra linear e matrizes de permutação.

## Descrição

Esta biblioteca implementa uma versão digital da máquina Enigma usando conceitos de álgebra linear:
- **One-hot encoding**: Representação de caracteres como vetores
- **Matrizes de permutação**: Uso de multiplicação matricial para cifragem
- **Enigma**: Implementação da máquina Enigma onde o alfabeto cifrado é permutado a cada caractere

## Instalação

### Requisitos

- Python 3.8 ou superior
- NumPy

### Instalação via pip

```bash
pip install -e .
```

Ou, se preferir instalar diretamente:

```bash
pip install numpy
```

E então importe o módulo diretamente:

```python
from enigma_lib import enigma, cifrar, decifrar
```

## Uso Básico

### Cifra de Substituição Simples

```python
from enigma_lib import cifrar, decifrar

alfabeto_normal = "abcdefghijklmnopqrstuvwxyz "
alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"

# Cifrar
mensagem_cifrada = cifrar(mensagem, alfabeto_normal, alfabeto_cifrado)
print(mensagem_cifrada)

# Decifrar
mensagem_recuperada = decifrar(mensagem_cifrada, alfabeto_cifrado, alfabeto_normal)
print(mensagem_recuperada)
```

### Máquina Enigma

```python
from enigma_lib import enigma, enigma_decifrar

alfabeto_normal = "abcdefghijklmnopqrstuvwxyz "
alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"
mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"

# Cifrar com Enigma
mensagem_cifrada = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
print(mensagem_cifrada)

# Decifrar
mensagem_recuperada = enigma_decifrar(mensagem_cifrada, alfabeto_normal, 
                                      alfabeto_cifrado, cifrador_auxiliar)
print(mensagem_recuperada)
```

### Operações Matriciais

```python
from enigma_lib import (
    char_to_one_hot,
    message_to_matrix,
    alphabet_to_permutation_matrix,
    permutation_matrix_to_alphabet
)
import numpy as np

alfabeto = "abc"

# Converter caractere para vetor one-hot
vetor_a = char_to_one_hot('a', alfabeto)
print(vetor_a)  # [[1], [0], [0]]

# Converter mensagem para matriz
M = message_to_matrix("aabbcc", alfabeto)
print(M)

# Criar matriz de permutação
P = alphabet_to_permutation_matrix("abc", "bca")
print(P)

# Aplicar permutação
M_cifrada = P @ M
print(M_cifrada)

# Converter matriz de permutação de volta para alfabeto
alfabeto_recuperado = permutation_matrix_to_alphabet(P, "abc")
print(alfabeto_recuperado)  # "bca"
```

## Estrutura do Projeto

```
enigma_lib/
├── __init__.py      # Inicialização do pacote
└── enigma.py        # Implementação principal
```

## Funções Principais

### Funções de Conversão

- `char_to_one_hot(char, alphabet)`: Converte um caractere em vetor one-hot
- `message_to_matrix(message, alphabet)`: Converte uma mensagem em matriz
- `alphabet_to_permutation_matrix(alphabet_normal, alphabet_cifrado)`: Cria matriz de permutação
- `permutation_matrix_to_alphabet(P, alphabet_normal)`: Converte matriz de permutação para alfabeto

### Funções de Criptografia

- `cifrar(mensagem_entrada, alphabet_normal, alphabet_cifrado)`: Cifra usando substituição simples
- `decifrar(mensagem_cifrada, alphabet_cifrado, alphabet_normal)`: Decifra mensagem
- `enigma(mensagem_entrada, alphabet_normal, alphabet_cifrado, cifrador_auxiliar)`: Cifra usando Enigma
- `enigma_decifrar(mensagem_cifrada, alphabet_normal, alphabet_cifrado, cifrador_auxiliar)`: Decifra mensagem Enigma

## Fundamentos Matemáticos

### One-Hot Encoding

Cada caractere é representado como um vetor coluna onde apenas um elemento é 1 e os demais são 0:

$$
A = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad
B = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad
C = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
$$

### Matriz de Permutação

Uma mensagem $M$ é cifrada multiplicando por uma matriz de permutação $P$:

$$
P \cdot M = M_c
$$

Para decifrar, usamos a inversa:

$$
M = P^{-1} \cdot M_c
$$

### Máquina Enigma

A máquina Enigma aplica uma permutação diferente a cada caractere, tornando a criptografia mais segura. Após cada caractere cifrado, o alfabeto cifrado é permutado usando o cifrador auxiliar.

## Exemplos

Veja o arquivo `exemplo.py` para exemplos mais detalhados de uso.

## Licença

Este projeto é para fins educacionais.

## Autor

Implementado como parte do curso de Álgebra Linear.

