from django.db import models

# Create your models here.

#add the cat class & list and view function below the imports
# class Cat: #parenthesis is optional if not inheriting from another class
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

class Cat(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    description = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Collector(models.Model):
    collector_name = models.CharField(max_length=200)

    def __str__(self):
        return self.collector_name

class Collection(models.Model):
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE, related_name='collections')
    breeds = models.TextField()
    num_of_cats = models.IntegerField()
    looking_for = models.TextField()

    def __str__(self):
        return self.collector

cats = [
    Cat('Lolo', 'tabby', 'foul little demon', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]