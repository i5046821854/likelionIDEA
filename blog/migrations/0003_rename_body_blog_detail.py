# Generated by Django 3.2.2 on 2021-06-29 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='body',
            new_name='detail',
        ),
    ]