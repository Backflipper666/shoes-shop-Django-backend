# Generated by Django 4.2.3 on 2023-07-15 06:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0003_rename_name_shoe_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='color',
            field=models.CharField(default='white', max_length=50),
        ),
        migrations.AddField(
            model_name='shoe',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='shoe',
            name='discountPercent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='shoe',
            name='gender',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women'), ('kids', 'Kids')], default='men', max_length=10),
        ),
        migrations.AddField(
            model_name='shoe',
            name='image',
            field=models.ImageField(default='', upload_to='shoe_images/'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='image2',
            field=models.ImageField(blank=True, upload_to='shoe_images/'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='image3',
            field=models.ImageField(blank=True, upload_to='shoe_images/'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='image4',
            field=models.ImageField(blank=True, upload_to='shoe_images/'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='material',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='shoe',
            name='newCollection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shoe',
            name='onSale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shoe',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='shoe',
            name='season',
            field=models.CharField(blank=True, choices=[('summer', 'Summer'), ('winter', 'Winter'), ('demi', 'Demi')], max_length=10),
        ),
        migrations.AddField(
            model_name='shoe',
            name='size',
            field=models.IntegerField(default=40),
        ),
        migrations.AddField(
            model_name='shoe',
            name='stock',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='brand',
            field=models.CharField(choices=[('FILA', 'FILA'), ('Nike', 'Nike'), ('Adidas', 'Adidas'), ('Puma', 'Puma'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='old_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]