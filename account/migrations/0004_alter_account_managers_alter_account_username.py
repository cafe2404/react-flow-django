# Generated by Django 5.1.2 on 2024-11-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_email_alter_account_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
