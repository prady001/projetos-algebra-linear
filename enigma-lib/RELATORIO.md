# Relatório: Implementação da Máquina Enigma usando Álgebra Linear

## 1. Introdução

Este relatório descreve a implementação matemática de uma máquina Enigma digital usando conceitos de álgebra linear, especificamente matrizes de permutação e operações matriciais.

## 2. Fundamentos Matemáticos

### 2.1 One-Hot Encoding

O primeiro passo é representar caracteres como vetores. Usamos **one-hot encoding**, onde cada caractere é representado como uma matriz-coluna onde todos os elementos são zero, exceto o elemento correspondente ao caractere no alfabeto, que é 1.

Para um alfabeto de 3 letras (a, b, c), temos:

$$
A = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad
B = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad
C = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
$$

**Implementação no código:**
- Função `char_to_one_hot(char, alphabet)` em `enigma.py` (linhas 10-40)
- Cria um vetor zero de tamanho `len(alphabet)` e define `one_hot[idx, 0] = 1` onde `idx` é a posição do caractere no alfabeto

### 2.2 Representação de Mensagens como Matrizes

Uma mensagem pode ser representada como uma matriz $M \in \mathbb{R}^{N \times T}$, onde:
- $N$ é o número de caracteres no alfabeto
- $T$ é o número de caracteres na mensagem

Cada coluna da matriz é um vetor one-hot representando um caractere da mensagem.

Exemplo: A mensagem "AABBCC" seria representada como:

$$
M = \begin{bmatrix}
1 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 1
\end{bmatrix}
$$

**Implementação no código:**
- Função `message_to_matrix(message, alphabet)` em `enigma.py` (linhas 43-70)
- Cria uma matriz concatenando vetores one-hot horizontalmente usando `np.hstack()`

### 2.3 Matrizes de Permutação

Uma **matriz de permutação** $P$ é uma matriz quadrada onde cada linha e cada coluna contém exatamente um elemento 1 e os demais são 0. Quando multiplicamos uma matriz de permutação por uma mensagem, estamos permutando as linhas da mensagem.

Se multiplicarmos a matriz identidade $I$ por uma mensagem $M$, obtemos a própria mensagem:

$$
I \cdot M = M
$$

Porém, se permutarmos as linhas de $I$ para formar uma matriz de permutação $P$, obtemos uma mensagem cifrada:

$$
P \cdot M = M_c
$$

**Implementação no código:**
- Função `alphabet_to_permutation_matrix(alphabet_normal, alphabet_cifrado)` em `enigma.py` (linhas 73-108)
- Para cada caractere no alfabeto normal na posição $i$, encontra sua posição $j$ no alfabeto cifrado
- Define $P[j, i] = 1$ para criar a matriz de permutação

### 2.4 Decifragem usando a Inversa

Para decifrar, usamos a inversa da matriz de permutação:

$$
\begin{aligned}
P \cdot M &= M_c \\
P^{-1} \cdot P \cdot M &= P^{-1} \cdot M_c \\
I \cdot M &= P^{-1} \cdot M_c \\
M &= P^{-1} \cdot M_c
\end{aligned}
$$

Para uma matriz de permutação, a inversa é simplesmente a transposta: $P^{-1} = P^T$.

**Implementação no código:**
- Função `permutation_matrix_to_alphabet(P, alphabet_normal)` em `enigma.py` (linhas 111-130)
- Encontra a posição do 1 em cada coluna da matriz para recuperar o alfabeto cifrado

## 3. Cifra de Substituição Simples

A cifra de substituição simples substitui cada caractere da mensagem por seu correspondente no alfabeto cifrado. Esta é uma operação direta sem uso de matrizes, mas serve como base para a máquina Enigma.

**Implementação no código:**
- Função `cifrar(mensagem_entrada, alphabet_normal, alphabet_cifrado)` em `enigma.py` (linhas 133-155)
- Função `decifrar(mensagem_cifrada, alphabet_cifrado, alphabet_normal)` em `enigma.py` (linhas 158-175)

## 4. Máquina Enigma

### 4.1 Princípio de Funcionamento

A máquina Enigma melhora a segurança da cifra de substituição aplicando uma **permutação diferente a cada caractere**. Após cada caractere cifrado, o alfabeto cifrado é permutado usando um cifrador auxiliar. Isso significa que a mesma letra na mensagem original pode ser cifrada de formas diferentes dependendo de sua posição.

### 4.2 Algoritmo

1. Para cada caractere $c_i$ na mensagem:
   - Encontra o índice $j$ de $c_i$ no alfabeto normal
   - Usa o caractere na posição $j$ do alfabeto cifrado atual
   - Adiciona esse caractere à mensagem cifrada
   - Permuta o alfabeto cifrado usando o cifrador auxiliar

2. Para decifrar:
   - Para cada caractere cifrado $c'_i$:
     - Encontra o índice $j$ de $c'_i$ no alfabeto cifrado atual
     - Usa o caractere na posição $j$ do alfabeto normal
     - Adiciona esse caractere à mensagem decifrada
     - Permuta o alfabeto cifrado da mesma forma (usando o mesmo cifrador auxiliar)

**Implementação no código:**
- Função `enigma(mensagem_entrada, alphabet_normal, alphabet_cifrado, cifrador_auxiliar)` em `enigma.py` (linhas 203-248)
- Função `enigma_decifrar(mensagem_cifrada, alphabet_normal, alphabet_cifrado, cifrador_auxiliar)` em `enigma.py` (linhas 251-283)

### 4.3 Versão Matricial

A máquina Enigma também pode ser implementada usando operações matriciais puras. Para cada caractere:
1. Converte o caractere para vetor one-hot
2. Aplica a matriz de permutação atual: $v_{cifrado} = P_{atual} \cdot v_{original}$
3. Atualiza a matriz de permutação para o próximo caractere

**Implementação no código:**
- Função `enigma_matricial(mensagem_entrada, alphabet_normal, alphabet_cifrado, cifrador_auxiliar)` em `enigma.py` (linhas 286-330)
- Retorna tanto a mensagem cifrada quanto as matrizes de permutação usadas para cada caractere

## 5. Mapeamento Código ↔ Matemática

| Conceito Matemático | Implementação no Código | Localização |
|---------------------|------------------------|-------------|
| Vetor one-hot | `char_to_one_hot()` | `enigma.py:10-40` |
| Matriz de mensagem $M$ | `message_to_matrix()` | `enigma.py:43-70` |
| Matriz de permutação $P$ | `alphabet_to_permutation_matrix()` | `enigma.py:73-108` |
| Multiplicação $P \cdot M$ | `P @ M` (usando NumPy) | `enigma_matricial()` |
| Inversa $P^{-1}$ | `permutation_matrix_to_alphabet()` | `enigma.py:111-130` |
| Cifra de substituição | `cifrar()` | `enigma.py:133-155` |
| Máquina Enigma | `enigma()` | `enigma.py:203-248` |
| Decifragem Enigma | `enigma_decifrar()` | `enigma.py:251-283` |

## 6. Exemplo Numérico

Considere:
- Alfabeto normal: `"abc"`
- Alfabeto cifrado inicial: `"bca"`
- Cifrador auxiliar: `"cab"`
- Mensagem: `"abc"`

### Passo 1: Caractere 'a'
- Índice de 'a' no alfabeto normal: 0
- Caractere na posição 0 do alfabeto cifrado atual (`"bca"`): 'b'
- Mensagem cifrada: `"b"`
- Novo alfabeto cifrado: cifrar(`"bca"`, `"abc"`, `"cab"`) = `"cab"`

### Passo 2: Caractere 'b'
- Índice de 'b' no alfabeto normal: 1
- Caractere na posição 1 do alfabeto cifrado atual (`"cab"`): 'a'
- Mensagem cifrada: `"ba"`
- Novo alfabeto cifrado: cifrar(`"cab"`, `"abc"`, `"cab"`) = `"abc"`

### Passo 3: Caractere 'c'
- Índice de 'c' no alfabeto normal: 2
- Caractere na posição 2 do alfabeto cifrado atual (`"abc"`): 'c'
- Mensagem cifrada: `"bac"`

Resultado: `"abc"` → `"bac"`

## 7. Conclusão

A implementação da máquina Enigma usando álgebra linear demonstra como conceitos matemáticos fundamentais (vetores, matrizes, permutações) podem ser aplicados em criptografia. A representação matricial permite uma compreensão clara do processo de cifragem e decifragem, além de facilitar a implementação computacional.

A biblioteca implementada fornece tanto uma interface simples (usando strings) quanto uma interface matricial completa, permitindo que o usuário escolha o nível de abstração mais adequado para sua aplicação.

