from django.db import models
from datetime import date

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    co_author = models.CharField(max_length=50, blank=True)
    register_date = models.DateField(default=date.today)
    borrowed = models.BooleanField(default=False)
    name_borrowed = models.CharField(max_length=50, blank=True, null=True)
    loan_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    running_time = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Book"

    def  __str__(self):
        return self.name
