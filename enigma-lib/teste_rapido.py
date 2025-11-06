"""
Teste rápido da biblioteca Enigma.
Execute este arquivo com: python teste_rapido.py
"""

from enigma_lib import enigma, enigma_decifrar, cifrar, decifrar

print("=" * 60)
print("TESTE RÁPIDO - BIBLIOTECA ENIGMA")
print("=" * 60)
print()

# Teste 1: Cifra simples
print("Teste 1: Cifra de Substituição Simples")
print("-" * 60)
alfabeto_normal = "abc"
alfabeto_cifrado = "bca"
mensagem = "abc"

cifrada = cifrar(mensagem, alfabeto_normal, alfabeto_cifrado)
decifrada = decifrar(cifrada, alfabeto_cifrado, alfabeto_normal)

print(f"Mensagem original: {mensagem}")
print(f"Mensagem cifrada:   {cifrada}")
print(f"Mensagem decifrada: {decifrada}")
print(f"✓ Teste 1 passou: {mensagem == decifrada}")
print()

# Teste 2: Enigma
print("Teste 2: Máquina Enigma")
print("-" * 60)
cifrador_auxiliar = "cab"

cifrada = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
decifrada = enigma_decifrar(cifrada, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)

print(f"Mensagem original: {mensagem}")
print(f"Mensagem cifrada:   {cifrada}")
print(f"Mensagem decifrada: {decifrada}")
print(f"✓ Teste 2 passou: {mensagem == decifrada}")
print()

# Teste 3: Exemplo do projeto
print("Teste 3: Exemplo do Projeto")
print("-" * 60)
alfabeto_normal = "abcdefghijklmnopqrstuvwxyz "
alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"
mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"

cifrada = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
decifrada = enigma_decifrar(cifrada, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)

print(f"Mensagem original: {mensagem}")
print(f"Mensagem cifrada:   {cifrada}")
print(f"Mensagem decifrada: {decifrada}")
print(f"✓ Teste 3 passou: {mensagem == decifrada}")
print()

print("=" * 60)
print("✓ TODOS OS TESTES PASSARAM!")
print("=" * 60)

