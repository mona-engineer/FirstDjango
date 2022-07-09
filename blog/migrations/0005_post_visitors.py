# Generated by Django 3.2.13 on 2022-05-21 05:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_remove_postviewwithuniqueuser_viewers'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visitors',
            field=models.ManyToManyField(editable=False, related_name='post_visitor', to=settings.AUTH_USER_MODEL),
        ),
    ]