# Generated by Django 3.1.1 on 2020-09-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaounceApp', '0004_remove_image_imagefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pubDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
