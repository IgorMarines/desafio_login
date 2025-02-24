# Desafio Login

Este projeto é uma aplicação Django simples para registro, login e logout de usuários utilizando SQLite.

## Funcionalidades

### Tela de Login
- **Validação de credenciais:**
  - E-mail errado, mas existente no banco: "E-mail inválido"
  - Senha errada, mas existente no banco: "Senha inválida"
  - E-mail inexistente no banco: "E-mail inexistente"
  - Senha inexistente no banco: "Senha inexistente"
- **Campos obrigatórios:** O e-mail e a senha não podem estar vazios.
- **Redirecionamento:**
  - Ao fazer login com sucesso, o usuário é direcionado para a tela de "Menu".
  - O textbutton "Registrar" leva para a tela de "Registrar".

### Tela de Registro
- **Campos do formulário:**
  - Nome (apenas letras, valida erro se inválido).
  - E-mail (validação para aceitar apenas e-mails válidos com "@").
  - Senha (deve conter ao menos 8 caracteres, 1 caractere especial, 1 número e 1 letra maiúscula).
  - Confirmar senha (deve ser idêntico ao campo "senha").
- **Exibição de senha:**
  - Opção para visualizar ou ocultar a senha e a confirmação de senha.
- **Botões:**
  - "Registrar" para enviar o formulário.
  - "Cancelar" para voltar à tela de login.

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

### 6. Configurar o Envio de E-mails (Opcional)
Para habilitar o envio de e-mails de confirmação, crie um arquivo `.env` na raiz do projeto e configure suas credenciais SMTP:
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seuemail@gmail.com
EMAIL_HOST_PASSWORD=suasenha
EMAIL_USE_TLS=True
```
> **IMPORTANTE:** Caso essas configurações não sejam definidas no `.env`, nenhum e-mail de confirmação será enviado.
> Um arquivo `.env.example` está disponível para referência.

### 7. Rodar o Servidor
```bash
python manage.py runserver
```

Acesse o sistema em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Estrutura do Projeto
```
📺 desafio_login/
👉 desafio_login/      # Configuração do Django
👉 desafio_logins/     # Aplicação principal
👉 ll_env/            # (Ignorado) Virtual Environment
👉 db.sqlite3         # Banco de Dados SQLite
👉 manage.py          # Comandos Django
👉 requirements.txt   # Dependências do projeto
```

## Funcionalidades
- Registro de Usuário
- Login e Logout
- Proteção CSRF
- Mensagens de erro e sucesso
- Envio de e-mails de confirmação (caso configurado)

## Observações
- **A venv não deve ser enviada para o repositório!**
- **Certifique-se de rodar os comandos dentro da venv ativada.**

---
Se precisar de ajuda, entre em contato! 🚀

