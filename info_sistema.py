import os
import platform

print("=" * 40)
print("SISTEMA OPERACIONAL CONFIGURADO")
print("=" * 40)

# Coleta infos do Debian
usuario = os.getlogin()
kernel = platform.release()
arquitetura = platform.architecture()[0]

print(f"Ola, {usuario}!")
print(f"Sua VM Debian esta rodando o Kernel: {kernel}")
print(f"Arquitetura do sistema: {arquitetura}")
print("=" * 40)

