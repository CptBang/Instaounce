# Generated by Django 3.1.1 on 2020-09-01 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaounceApp', '0002_auto_20200901_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='imageFile',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
