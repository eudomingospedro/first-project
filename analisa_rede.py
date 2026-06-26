print("=" * 40)
print(" ANALISADOR DE ENDEREÇOS IP (RECON)")
print("=" * 40)

# 1. O script pede um dado para o operador e guarda na variável 'ip_alvo'
ip_alvo = input("Digite o endereço de IP para análise: ")

print(f"\n[+] Analisando o alvo: {ip_alvo}...")

# 2. Lógica de Decisão: Verificando se o texto começa com os padrões de rede interna
if ip_alvo.startswith("192.168.") or ip_alvo.startswith("10."):
    print("[!] ALERTA: Este é um endereço de REDE LOCAL (Privado).")
    print("[!] Esse dispositivo só está acessível dentro da sua própria rede interna.")
else:
    print("[+] IDENTIFICADO: Este parece ser um IP PÚBLICO (Internet).")
    print("[+] Em um cenário real, este alvo exigiria varreduras externas (ex: Nmap)."

print("=" * 40)
