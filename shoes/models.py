#models.py
from django.db import models
from django.utils import timezone
import os

def get_shoe_image_path(instance, filename):
    # Generate a unique filename based on the shoe's title and ID
    unique_filename = f"{instance.title}_{instance.id}{os.path.splitext(filename)[1]}"
    # Create a directory path based on the shoe's title and ID
    directory_path = os.path.join('shoe_images', f"{instance.title}_{instance.id}")
    # Return the full file path including the directory path
    return os.path.join(directory_path, unique_filename)



class Shoe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    brand = models.CharField(max_length=100, choices=[('FILA', 'FILA'), ('Nike', 'Nike'), ('Adidas', 'Adidas'), ('Puma', 'Puma'), ('Other', 'Other')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50, default='white')
    size = models.IntegerField(default=40)
    material = models.CharField(max_length=100, blank=True)
    stock = models.JSONField(default=dict)
    image = models.ImageField(upload_to=get_shoe_image_path, default='')
    image2 = models.ImageField(upload_to=get_shoe_image_path, default='')
    image3 = models.ImageField(upload_to=get_shoe_image_path, default='')
    image4 = models.ImageField(upload_to=get_shoe_image_path, default='')
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    createdAt = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=[('men', 'Men'), ('women', 'Women'), ('kids', 'Kids')], default='men')
    onSale = models.BooleanField(default=False)
    discountPercent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    newCollection = models.BooleanField(default=False)
    season = models.CharField(max_length=10, choices=[('summer', 'Summer'), ('winter', 'Winter'), ('demi', 'Demi')], blank=True)

    def save(self, *args, **kwargs):
        # If the shoe instance doesn't have an id (is not saved to the database yet),
        # save it to generate an id before saving the image
        if not self.id:
            super().save(*args, **kwargs)
        
        # Call the original save() method to save the image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title + ' ' + self.brand


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    permission_level = models.CharField(max_length=20)
    favorite_shoes = models.ManyToManyField('Shoe', related_name='users', blank=True)

    def __str__(self):
        return self.email
# . .venv/bin/activate

# python manage.py migrate shoes zero
# python manage.py makemigrations shoes
# python manage.py migrate shoes