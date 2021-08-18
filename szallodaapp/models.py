from django.db import models

# Create your models here.
class Login_staff(models.Model):
    user_name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)


class Registrationform(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    login =models.ForeignKey(Login_staff,on_delete=models.CASCADE)

class Login_customer(models.Model):
    customer_name = models.CharField(max_length = 100)
    table_no = models.CharField(max_length=3)
class Todays_special(models.Model):
    food_item = models.CharField(max_length = 100)
    price = models.CharField(max_length = 20)
    discount = models.CharField(max_length = 20)