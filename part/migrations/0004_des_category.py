# Generated by Django 3.0.2 on 2020-04-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0003_auto_20200409_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='des',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
