# Generated by Django 3.1 on 2024-08-18 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20240818_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email_history',
            old_name='email',
            new_name='user',
        ),
    ]
