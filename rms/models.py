from django.db import models

 
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField(max_length=225)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name