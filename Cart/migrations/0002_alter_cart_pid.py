# Generated by Django 3.2.8 on 2021-10-29 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_products_photo'),
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.products'),
        ),
    ]
