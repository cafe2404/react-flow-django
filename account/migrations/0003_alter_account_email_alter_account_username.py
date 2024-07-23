# Generated by Django 5.0.7 on 2024-07-23 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_account_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]