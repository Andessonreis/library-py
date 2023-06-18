from django.contrib import admin
from . models import Books, Book_category, Loan

# Register your models here.

admin.site.register(Books)
admin.site.register(Book_category)
admin.site.register(Loan)