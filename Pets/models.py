from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(unique=False)
    breed = models.CharField(max_length=255)
    gender = models.IntegerField(default=1)
    description = models.TextField()  
    posted_at = models.DateTimeField(auto_now_add=True)
    pet_image = models.ImageField(upload_to="category/",null=True, blank=True )
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.breed} and {self.category}"

class PetCategory(models.Model):
    category_image = models.ImageField(upload_to="category/", null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_image


