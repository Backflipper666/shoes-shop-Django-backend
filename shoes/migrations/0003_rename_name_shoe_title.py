# Generated by Django 4.2.3 on 2023-07-13 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='name',
            new_name='title',
        ),
    ]
