# Generated by Django 4.0.4 on 2022-06-22 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcategory',
            name='title_cat',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]