# Generated by Django 3.0.2 on 2020-04-23 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0006_auto_20200423_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='com',
            old_name='comment',
            new_name='comments',
        ),
    ]