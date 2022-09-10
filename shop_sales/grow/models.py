from django.db import models

from django.conf import settings

# Create your models here.

class Product(models.Model):
    date = models.CharField(max_length=100, blank=False)
    product_name = models.name = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField()
    selling_price = models.IntegerField()
    cost_price = models.IntegerField()
    customer_name = models.CharField(max_length=100, blank=False, null=False)
    customer_age = models.IntegerField()
    customer_gender = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f'{self.date} - {self.product_name} - {self.category} - {self.quantity} - {self.selling_price} - {self.cost_price} - {self.customer_name} - {self.customer_age}- {self.customer_gender}'


class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)