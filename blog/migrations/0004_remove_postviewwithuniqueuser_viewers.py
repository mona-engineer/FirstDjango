# Generated by Django 3.2.13 on 2022-05-20 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postviewwithuniqueuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postviewwithuniqueuser',
            name='viewers',
        ),
    ]
