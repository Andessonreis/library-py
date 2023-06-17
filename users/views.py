from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect
from hashlib import sha256

# Create your views here.


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def register(request):
    status = request.GET.get("status")
    return render(request, "register.html", {"status": status})


def validate_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    # session
    password = sha256(password.encode()).hexdigest()

    # veriica se o usuario existe no banco de dados
    user = User.objects.filter(email = email).filter(password = password)
    
    if len(user) == 0: # user não encontrado
        return redirect('/auth/login/?status=1')
    elif len(user) == 1:
        request.session['user'] = user[0].id # armazenando user em uma session(var globlal)
        return redirect(f'/book/home')

# recebendo a request dos valores na tela de register
def validate_signup(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")

    # filta se o objeto ja esta cadastrado
    user = User.objects.filter(email=email)

    if len(name.strip()) == 0 or len(email.strip()) == 0:
        return redirect("/auth/register/?status=1")

    if len(password.strip()) < 8:
        return redirect("/auth/register/?status=2")

    if len(user) > 0:
        return redirect("/auth/register/?status=3")

    try:
        ##criptografando a senha
        password = sha256(password.encode()).hexdigest()
        user = User(name=name, email=email, password=password)
        user.save()

        return redirect("/auth/register/?status=0")
    except:
        return redirect("/auth/login/?status=4")


def exit_user(request):
    request.session.flush()
    return redirect('/auth/login/')