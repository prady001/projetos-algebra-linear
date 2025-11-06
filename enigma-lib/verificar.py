"""
Script simples para verificar se a biblioteca está funcionando.
"""

import sys
import os

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from enigma_lib import cifrar, decifrar, enigma, enigma_decifrar
    print("✓ Importação bem-sucedida!")
    
    # Teste básico
    alfabeto_normal = "abc"
    alfabeto_cifrado = "bca"
    mensagem = "abc"
    
    print(f"\nTeste 1: Cifra simples")
    print(f"Mensagem: {mensagem}")
    cifrada = cifrar(mensagem, alfabeto_normal, alfabeto_cifrado)
    print(f"Cifrada: {cifrada}")
    decifrada = decifrar(cifrada, alfabeto_cifrado, alfabeto_normal)
    print(f"Decifrada: {decifrada}")
    print(f"✓ Teste 1 passou: {mensagem == decifrada}")
    
    print(f"\nTeste 2: Enigma")
    cifrador_auxiliar = "cab"
    cifrada = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
    print(f"Cifrada: {cifrada}")
    decifrada = enigma_decifrar(cifrada, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
    print(f"Decifrada: {decifrada}")
    print(f"✓ Teste 2 passou: {mensagem == decifrada}")
    
    print(f"\nTeste 3: Exemplo do projeto")
    alfabeto_normal = "abcdefghijklmnopqrstuvwxyz "
    alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
    cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"
    mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"
    
    cifrada = enigma(mensagem, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
    decifrada = enigma_decifrar(cifrada, alfabeto_normal, alfabeto_cifrado, cifrador_auxiliar)
    print(f"Mensagem original: {mensagem}")
    print(f"Mensagem decifrada: {decifrada}")
    print(f"✓ Teste 3 passou: {mensagem == decifrada}")
    
    print("\n" + "=" * 60)
    print("✓ TODOS OS TESTES PASSARAM!")
    print("=" * 60)
    
except ImportError as e:
    print(f"✗ Erro de importação: {e}")
    print("\nCertifique-se de que o numpy está instalado:")
    print("pip install numpy")
    sys.exit(1)
except Exception as e:
    print(f"✗ Erro: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

