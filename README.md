# 🔐 Gerenciador de Senhas em Python

Um simples gerenciador de senhas desenvolvido em Python com criptografia utilizando `Fernet` (biblioteca do `cryptography`). O sistema permite ao usuário salvar senhas criptografadas para diferentes domínios e visualizá-las quando necessário. Todas as senhas são armazenadas de forma local e segura em arquivos `.txt`.

---

## 📌 Funcionalidades

- Criação e armazenamento de senhas criptografadas com segurança.
- Armazenamento de senhas por domínio.
- Criação e gerenciamento de chaves de criptografia únicas.
- Armazenamento local dos dados em arquivos `.txt`.
- Interface por linha de comando (CLI).

---

## 🛠️ Tecnologias e Bibliotecas

- Python 3.10+
- [`cryptography`](https://cryptography.io/en/latest/) — para criptografar e descriptografar senhas.
- `pathlib`, `os`, `datetime` — para manipulação de arquivos, diretórios e datas.

---

## 🧾 Estrutura do Projeto

gerenciador-de-senhas/
├── model/
│ └── password.py # Classe Password que representa os dados e a lógica de persistência
│ └── base.py # Classe BaseModel que manipula os dados e criação de arquivos e informações
├── view/
│ └── password_view.py # Classe FernetHasher para criptografia
├── templates/
│ └── template.py # Script principal do projeto
├── db/ # Diretório onde as senhas são salvas
│ └── Password.txt # Arquivo de persistência local (criado automaticamente)
├── keys/
│ └── key_fLHza.key # Arquivo que é gerado automaticamente e armazena as chaves de cada senha e domínio
├── venv/ # Ambiente virtual (opcional)
└── README.md # Este arquivo