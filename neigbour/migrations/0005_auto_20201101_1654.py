# Generated by Django 3.1 on 2020-11-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neigbour', '0004_auto_20201101_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Profilephoto',
            field=models.ImageField(upload_to='users/'),
        ),
    ]
