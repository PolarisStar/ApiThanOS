# Generated by Django 2.1.4 on 2018-12-13 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_auto_20181213_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendedor',
            old_name='email_v',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='vendedor',
            old_name='password_v',
            new_name='password',
        ),
    ]
