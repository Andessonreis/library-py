from django.db import models
from datetime import date
import datetime
from users.models import User

# Create your models here.

class Book_category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100 )
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
    CHOICES = (
        ('P', 'Poor'),
        ('R', 'Regular'),
        ('G', 'Good'),
        ('E', 'Excellent'),
    )

    name_borrowed = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    loan_date = models.DateTimeField(default=datetime.datetime.now())
    return_date = models.DateTimeField(blank=True, null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    evaluation = models.CharField(max_length=1, blank=True, null=True, choices=CHOICES)

    def  __str__(self):
        return f"{self.name_borrowed} | {self.book}"




