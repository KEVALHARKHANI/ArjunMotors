# Generated by Django 3.1.2 on 2020-10-24 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='catageries',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='qauntitie',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='products',
            name='model',
        ),
    ]
