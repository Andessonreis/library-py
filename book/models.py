from django.db import models

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    co_author = models.CharField(max_length=50)
    register_date = models.DateField()
    borrowed = models.BooleanField(default=False)
    name_borrowed = models.CharField(max_length=50)
    loan_date = models.DateTimeField()
    return_date = models.DateTimeField()
    running_time = models.DateField()
