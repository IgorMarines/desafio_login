import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import User

def is_valid_email(email):
    """Verifica se o e-mail é válido"""
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def is_valid_password(password):
    """Valida a senha com os critérios de segurança"""
    return (
        len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "!@#$%^&*()-_+=<>?/|{}[]" for c in password)
    )

def is_valid_name(name):
    """Verifica se o nome contém apenas letras e espaços"""
    return bool(re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", name))

def register(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        confirm_password = request.POST.get("confirm_password", "").strip()

        print(f"Recebido: Nome={name}, Email={email}, Senha={password}")

        # Validação do nome
        if not is_valid_name(name):
            messages.error(request, "O nome deve conter apenas letras.")
            return redirect("register")

        # Validação do e-mail
        if not is_valid_email(email):
            messages.error(request, "E-mail inválido. Insira um e-mail válido.")
            return redirect("register")

        # Verifica se o e-mail já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está em uso.")
            return redirect("register")

        # Validação da senha
        if not is_valid_password(password):
            messages.error(request, "A senha deve ter pelo menos 8 caracteres, incluindo uma letra maiúscula, um número e um caractere especial.")
            return redirect("register")

        # Validação da confirmação de senha
        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect("register")

        try:
            # Criptografa a senha e salva o usuário
            hashed_password = make_password(password)
            user = User.objects.create(username=name, email=email, password=hashed_password)
            print("Usuário salvo com sucesso!")
        except Exception as e:
            print("Erro ao salvar usuário:", e)
            messages.error(request, "Erro ao criar usuário. Tente novamente.")
            return redirect("register")

        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect("login")

    return render(request, "desafio_logins/register.html")

def index(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        # Se os campos estiverem vazios
        if not email or not password:
            messages.error(request, "Preencha todos os campos.")
            return redirect("login")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "E-mail inexistente")
            return redirect("login")

        # Verifica se a senha foi cadastrada (caso de conta sem senha)
        if not user.password:
            messages.error(request, "Senha inexistente")
            return redirect("login")

        # Verifica se a senha está correta
        if not check_password(password, user.password):
            messages.error(request, "Senha inválida")
            return redirect("login")

        # Se passou por todas as verificações, login bem-sucedido
        request.session["user_id"] = user.id
        messages.success(request, "Login realizado com sucesso!")
        return redirect("dashboard")  # Direciona para a tela de Menu

    return render(request, "desafio_logins/login.html")

def dashboard(request):
    user_id = request.session.get("user_id")
    print("Login user : " + str(user_id))
    if not user_id:
        messages.error(request, "Faça login para acessar o Dashboard.")
        return redirect("login")

    user = User.objects.get(id=user_id)
    return render(request, "desafio_logins/dashboard.html", {"user": user})

def logout(request):
    request.session.flush()
    messages.success(request, "Logout realizado com sucesso!")
    return redirect("login")