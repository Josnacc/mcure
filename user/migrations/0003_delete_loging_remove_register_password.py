# Generated by Django 4.1.1 on 2023-10-23 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_password_loging_password1_register_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Loging',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password',
        ),
    ]