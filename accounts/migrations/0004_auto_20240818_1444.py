# Generated by Django 3.1 on 2024-08-18 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_email_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email_history',
            old_name='user',
            new_name='user_email',
        ),
    ]