# Generated by Django 4.2.2 on 2023-06-09 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pub_year',
            new_name='pub_date',
        ),
    ]
