import os
import sys

print("=" * 40)
print("VERIFICADOR DE PRIVILEGIOS DE SEGURANÇA")
print("=" * 40)

# O módulo 'os' tem a função 'getuid()' que pega o ID do usúario atual.
usuario_id = os.getuid()

print(f"O ID do usúario atual é: {usuario_id}")

# Lógica de decisão (if/else)
if usuario_id == 0:
    print("[+] PERMISSÃO CONCEDIDA: Você está rodando como ROOT.")
    print("[+] Pronto para executar ferramentas avançadas de Cybersecurity.")

else:
    print("[-] ERRO: Acesso limitado.")
    print("[-] Este script precisa de privilégios de administrador (root).")
    print("[-] Dica: tente rodar com 'sudo python3 checa_privilegio.py'")

print("-" * 40)

