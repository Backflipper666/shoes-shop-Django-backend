# Generated by Django 4.2.3 on 2023-07-15 06:41

from django.db import migrations, models
import shoes.models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0004_shoe_color_shoe_createdat_shoe_discountpercent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='image',
            field=models.ImageField(default='', upload_to=shoes.models.get_shoe_image_path),
        ),
    ]