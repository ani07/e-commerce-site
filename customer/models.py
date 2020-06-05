from django.db import models

# Create your models here.
class Customers(models.Model):
    cust_id = models.AutoField(primary_key=True)
    person = models.CharField(max_length=128)
    organization = models.CharField(max_length=128)
    gender = models.CharField(max_length=2)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    mobile = models.IntegerField(max_length=128)
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128)
    address3 = models.CharField(max_length=128)
    address4 = models.CharField(max_length=128)
    zip = models.BigIntegerField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    person = models.CharField(max_length=128)
    person = models.CharField(max_length=128)

class ref_payment_methods(models.Model):
    payment_method_code = models.AutoField(primary_key=True)
    payment_method_des = models.CharField(max_length=256)

class cust_payments_methods(models.Model):
    cust_payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    payment_method_code = models.ForeignKey(ref_payment_methods,on_delete=models.CASCADE)
    card_number = models.CharField(max_length=24)
    name_on_card = models.CharField(max_length=256)
    expiry_date = models.DateField(auto_now=False)
    other_details = models.CharField(max_length=256)
