# Generated by Django 4.2.2 on 2023-06-23 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_alter_loan_loan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 15, 57, 32, 414757)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]