from django.db import models

# Create your models here.

class Service_Provider(models.Model):
    GENDER_OPTIONS={
        ("M","Male"),
        ("F","Female")}
    name = models.CharField(max_length= 30, verbose_name="Provider Name")
    service = models.CharField(max_length= 20)
    contact = models.CharField(max_length= 10)
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    location = models.CharField(max_length= 20, null= True, blank=True, default="N/A")

class Policy(models.Model):
    policy_name = models.CharField(max_length=30)
    Service_Provider = models.ForeignKey(Service_Provider,on_delete=models.CASCADE)
    benefits = models.CharField(max_length=40)
    lapse_period = models.CharField(max_length=30)
    cost = models.IntegerField()

     
class Customer(models.Model):
    customer_name = models.CharField(max_length= 20)
    customer_contact = models.CharField(max_length= 10)
    policy = models.ForeignKey(Policy,default=False,on_delete=models.CASCADE)
    Service_Provider = models.ForeignKey(Service_Provider,on_delete=models.CASCADE)
    service_date =models.DateField(auto_now=False, auto_now_add= False)
    service_recieved= models.BooleanField(default=False)


class Payment(models.Model):
    payment_date = models.DateField(auto_now=False, auto_now_add= False)
    policy = models.ForeignKey(Policy,default=False,on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,default=False,on_delete=models.CASCADE)
    amount_paid = models.IntegerField(default=False)


    


    
