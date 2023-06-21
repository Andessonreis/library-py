# Generated by Django 4.2.2 on 2023-06-18 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('book', '0003_book_category_books_user_books_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_category',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.user'),
            preserve_default=False,
        ),
    ]