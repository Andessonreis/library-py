# Generated by Django 4.2.2 on 2023-06-15 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('co_author', models.CharField(max_length=50)),
                ('register_date', models.DateField()),
                ('borrowed', models.BooleanField(default=False)),
                ('name_borrowed', models.CharField(max_length=50)),
                ('loan_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('running_time', models.DateField()),
            ],
        ),
    ]
