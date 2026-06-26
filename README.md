Markdown
￼
￼
# Meu Aprendizado em Linux

Este repositório foi criado para documentar minha jornada de estudos unindo Linux (Debian), desenvolvimento em Python e fundamentos de Cybersecurity/Cloud Security.

## Projetos Desenvolvidos

### Nível 1: Fundamentos e Reconhecimento
* **info_sistema.py**: Um script em Python que faz o reconhecimento (*recon*) básico do sistema operacional, coletando o nome do usuário logado, versão do Kernel Linux e arquitetura do sistema utilizando as bibliotecas nativas `os` e `platform`.
* **checa_privilegio.py**: Um script que utiliza lógica de decisão (`if/else`) e a função `os.getuid()` para identificar se o exectuor possui privilégios de administrador (`root`), simulando a validação inicial de ferramentas de Cybersecurity.
* **analisa_rede.py**: Um script que interage com o operador através da função `input()` para capturar um endereço IP. Utiliza os métodos de manipulação de string (`.startswith()`) e o operador lógico `or` para classificar dinamicamente se o alvo pertence a uma rede local/privada (como as faixas `192.168.X.X` ou `10.X.X.X`) ou a uma rede pública na internet, simulando a triagem inicial de uma etapa de Reconhecimento (*Recon*).
 
## Aprendizados da Semana
* Configuração e versionamento de código com Git e GitHub utilizando chaves PAT (Tokens).
* Manipulação de arquivos via terminal Linux utilizando o editor de texto nativo `nano`.
* Conceito de *Reconnaissance* (Reconhecimento de ambiente) em testes de invasão.
