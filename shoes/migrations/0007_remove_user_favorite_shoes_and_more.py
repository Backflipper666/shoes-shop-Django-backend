# Generated by Django 4.2.3 on 2023-07-16 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0006_alter_shoe_image2_alter_shoe_image3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorite_shoes',
        ),
        migrations.RemoveField(
            model_name='user',
            name='permission_level',
        ),
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(blank=True, related_name='users_cart', to='shoes.shoe'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='users_favorited', to='shoes.shoe'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
