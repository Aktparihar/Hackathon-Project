# Generated by Django 2.2.13 on 2021-01-18 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20210118_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='login',
            new_name='name',
        ),
    ]
