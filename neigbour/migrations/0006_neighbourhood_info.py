# Generated by Django 3.1 on 2020-11-02 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neigbour', '0005_auto_20201101_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='Info',
            field=models.TextField(default='Yes', max_length=500),
            preserve_default=False,
        ),
    ]
