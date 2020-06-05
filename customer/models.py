from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.
class Customers(models.Model):
    cust_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=2)
    dob = models.DateField()
    email = models.CharField(max_length=128)
    mobile = models.IntegerField()
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128)
    address3 = models.CharField(max_length=128)
    address4 = models.CharField(max_length=128)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=128)
    auth_user_id = models.OneToOneField(AuthUser, models.DO_NOTHING, db_column="auth_user_id", related_name='customers')
    class Meta:
        managed = True
        db_table = "Customers"

    

class ref_payment_methods(models.Model):
    payment_method_code = models.IntegerField(primary_key=True)
    payment_method_des = models.CharField(max_length=256)
    class Meta:
        managed = True
        db_table = "Ref_payment_methods"

class cust_payments_methods(models.Model):
    cust_payment_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    payment_method_code = models.ForeignKey(ref_payment_methods,on_delete=models.CASCADE)
    card_number = models.CharField(max_length=24)
    name_on_card = models.CharField(max_length=256)
    expiry_date = models.DateField(auto_now=False)
    other_details = models.CharField(max_length=256)
    class Meta:
        managed = True
        db_table = "Cust_Payments_Methods"