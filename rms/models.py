from django.db import models
# djanog's default user model
from django.contrib.auth import get_user_model

User = get_user_model()
 
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
    
class Table(models.Model):
    number = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table number: {self.number}"
    
class Order(models.Model):
    PENDING = 'P'
    COMPLETED = 'C'
    STATUS_CHOICE = {
            PENDING: 'Pending',
            COMPLETED: 'Completed'
        }
    
    PAID = 'P'
    UNPAID = 'U'
    PAYMENT_CHOICE = {
        PAID: 'Paid',
        UNPAID: 'Not paid'
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=PENDING)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICE, default=PENDING)

    def __str__(self):
        return f"{self.user} - {self.status}"

class OrderItems(models.Model):
    food = models.ForeignKey(Food, on_delete=models.PROTECT, related_name='items')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')

    def __str__(self):
        return f"{self.order} - {self.food}"