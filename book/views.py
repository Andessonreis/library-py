from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import User
# Create your views here.

def home(request):
    if request.session.get("user"):
        user = User.objects.get(id = request.session['user']).name
        return HttpResponse(f"Salve de novo {user}")
    else:
        return redirect('/auth/login/?status=2')
