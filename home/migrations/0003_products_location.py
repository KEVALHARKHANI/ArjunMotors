# Generated by Django 3.1.2 on 2020-10-26 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201024_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='location',
            field=models.CharField(default='a1', max_length=50),
            preserve_default=False,
        ),
    ]