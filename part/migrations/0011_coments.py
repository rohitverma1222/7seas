# Generated by Django 3.0.2 on 2020-04-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0010_com'),
    ]

    operations = [
        migrations.CreateModel(
            name='coments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('comments', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]