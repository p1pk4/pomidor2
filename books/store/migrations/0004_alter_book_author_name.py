# Generated by Django 4.0.4 on 2022-04-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_book_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(max_length=255),
        ),
    ]