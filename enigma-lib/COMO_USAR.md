# Como Usar a Biblioteca Enigma

## Problema: Executar Python no PowerShell

Se você tentou executar código Python diretamente no PowerShell e recebeu um erro, isso acontece porque o PowerShell não é um interpretador Python. Você precisa executar o código Python de uma das seguintes formas:

## Opção 1: Executar um Script Python

No PowerShell, navegue até a pasta do projeto e execute:

```powershell
python exemplo.py
```

ou

```powershell
python verificar.py
```

ou

```powershell
python test_enigma.py
```

## Opção 2: Usar o Interpretador Python Interativo

1. Abra o PowerShell
2. Execute `python` (sem argumentos)
3. Isso abrirá o interpretador Python interativo
4. Agora você pode executar:

```python
from enigma_lib import enigma, cifrar, decifrar

alfabeto_normal = "abcdefghijklmnopqrstuvwxyz "
alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"
mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"

# Cifrar
cifrada = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
print(cifrada)

# Decifrar
decifrada = enigma_decifrar(cifrada, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
print(decifrada)
```

5. Para sair, digite `exit()` ou pressione `Ctrl+Z` seguido de `Enter`

## Opção 3: Executar Código Python Inline

No PowerShell, você pode executar código Python inline usando:

```powershell
python -c "from enigma_lib import enigma; print(enigma('abc', 'abc', 'bca', 'cab'))"
```

## Opção 4: Criar um Script Python e Executar

1. Crie um arquivo `meu_teste.py` com o código Python
2. Execute: `python meu_teste.py`

## Exemplo Completo

Crie um arquivo chamado `teste_rapido.py`:

```python
from enigma_lib import enigma, enigma_decifrar

alfabeto_normal = "abcdefghijklmnopqrstuvwxyz "
alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"
mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"

print("Mensagem original:", mensagem)

# Cifrar
cifrada = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
print("Mensagem cifrada:", cifrada)

# Decifrar
decifrada = enigma_decifrar(cifrada, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
print("Mensagem decifrada:", decifrada)
print("✓ Funcionou!" if mensagem == decifrada else "✗ Erro!")
```

Execute no PowerShell:

```powershell
python teste_rapido.py
```

## Resumo

- **PowerShell** = Shell do Windows (para comandos do sistema)
- **Python** = Interpretador Python (para código Python)
- Para executar código Python, use `python nome_do_arquivo.py` ou `python` para entrar no modo interativo

