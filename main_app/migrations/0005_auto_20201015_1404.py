# Generated by Django 3.1.2 on 2020-10-15 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201014_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='craft',
            old_name='material',
            new_name='materials',
        ),
    ]
