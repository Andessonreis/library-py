from django.contrib import admin
from users.models import User
# Register your models here.

#o admin não pode mudar os campos
@admin.register(User)
class User_admin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'password')