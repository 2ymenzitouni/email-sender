# Generated by Django 3.1 on 2024-08-18 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20240818_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email_history',
            old_name='user_email',
            new_name='email',
        ),
    ]