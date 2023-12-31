# Generated by Django 4.2.2 on 2023-06-15 02:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Book'},
        ),
        migrations.AlterField(
            model_name='books',
            name='co_author',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='loan_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='name_borrowed',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='register_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='books',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='running_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
