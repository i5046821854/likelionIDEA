# Generated by Django 3.2.2 on 2021-06-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_customuser_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='lat',
            field=models.FloatField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lng',
            field=models.FloatField(default='0', max_length=50),
        ),
    ]
