from django.db import models
from datetime import date
from users.models import User

# Create your models here.

class Book_category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name
    

class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    co_author = models.CharField(max_length=50, blank=True)
    register_date = models.DateField(default=date.today)
    borrowed = models.BooleanField(default=False)
    book_category = models.ForeignKey(Book_category, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Book"

    def  __str__(self):
        return self.name

class Loan(models.Model):
    name_borrowed = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    #name_borrowed = models.CharField(max_length=50, blank=True, null=True)
    loan_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Books, on_delete=models.DO_NOTHING)

    def  __str__(self):
        return f"{self.name_borrowed} | {self.book}"




