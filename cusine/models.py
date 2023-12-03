from django.db import models

# Create your models here.

# create a model with following fields
# "recipename": "Cookies",
#         "image": "https://images-gmi-pmc.edge-generalmills.com/087d17eb-500e-4b26-abd1-4f9ffa96a2c6.jpg",
#         "cuisines": "American",
#         "difficulty": "Easy",
#         "preptime": "45 minutes",
#         "cooktime": "15 minutes",
#         "ingredients": "Flour, butter, chocolate chips",
#         "directions": "Mix all the ingredients, shape cookies and bake!",
#         "description": "Goes well with a glass of milk or a cup of coffee.",


class Recipe(models.Model):
    recipename = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    cuisines = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    preptime = models.CharField(max_length=100)
    cooktime = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    directions = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.recipename
