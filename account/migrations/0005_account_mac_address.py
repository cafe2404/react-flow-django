# Generated by Django 5.1.2 on 2024-11-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_managers_alter_account_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='mac_address',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
    ]