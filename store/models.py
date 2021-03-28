from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Merchant(models.Model):
    merchant_name = models.CharField(max_length=15)

    def __str__(self):
        return self.merchant_name


class Category(models.Model):
    name = models.CharField(max_length=50)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} by {self.merchant}"


class AnimalCategory(models.Model):

    class Animal(models.TextChoices):
        DOG = 'Dog'
        CAT = 'Cat'
        HAMSTER = 'Hamster'

    animal = models.CharField(max_length=25, choices=Animal.choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.animal} {self.category}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    animalCategory = models.ForeignKey(AnimalCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    details = models.TextField(default="Insert details here...")
    ingredients = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.animalCategory.category.merchant})"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=5)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product review of {self.product} by {self.user}"

