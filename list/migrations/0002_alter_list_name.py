# Generated by Django 3.2.2 on 2021-06-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
