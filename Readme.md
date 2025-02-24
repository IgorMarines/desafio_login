# Desafio Login

Este projeto é uma aplicação Django simples para registro, login e logout de usuários utilizando SQLite.

## Tecnologias Utilizadas
- Python
- Django
- SQLite
- Virtual Environment (venv)

## Como Configurar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/IgorMarines/desafio_login.git
cd desafio_login
```

### 2. Criar e Ativar o Ambiente Virtual
```bash
python -m venv venv  # Criar venv (Windows/Linux/Mac)
```
**Ativar a venv:**
- **Windows (cmd/powershell):**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Aplicar Migrações do Banco de Dados
```bash
python manage.py migrate
```

### 5. Criar um Superusuário (Opcional)
```bash
python manage.py createsuperuser
```

### 6. Rodar o Servidor
```bash
python manage.py runserver
```

Acesse o sistema em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Estrutura do Projeto
```
📂 desafio_login/
│-- 📂 desafio_login/      # Configuração do Django
│-- 📂 desafio_logins/     # Aplicação principal
│-- 📂 ll_env/            # (Ignorado) Virtual Environment
│-- 📂 db.sqlite3         # Banco de Dados SQLite
│-- 📜 manage.py          # Comandos Django
│-- 📜 requirements.txt   # Dependências do projeto
```

## Funcionalidades
- Registro de Usuário
- Login e Logout
- Proteção CSRF
- Mensagens de erro e sucesso

## Observações
- **A venv não deve ser enviada para o repositório!**
- **Certifique-se de rodar os comandos dentro da venv ativada.**

---
Se precisar de ajuda, entre em contato! 🚀

