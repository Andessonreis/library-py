from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('validate_signup/', views.validate_signup, name='validate_signup'),
    path('validate_login/', views.validate_login, name='validate_login'),
]