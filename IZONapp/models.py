
# models.py
from django.db import models 
from django.contrib.auth import get_user_model
from django.utils import timezone

class LoginAttempt(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    username_attempted = models.CharField(max_length=150)
    timestamp = models.DateTimeField(default=timezone.now)
    successful = models.BooleanField(default=False)

    def __str__(self):
        return f"Login attempt by {self.username_attempted} on {self.timestamp}"
    


class Categoryproduct(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
  
    
    def __str__(self):
        return self.name
    




class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
   

    def __str__(self):
        return self.title or "Gallery Image"
    


class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f"ImageUpload {self.id}"  # Just to provide a string representation
