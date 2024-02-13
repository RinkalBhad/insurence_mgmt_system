from django.db import models

# Create your models here.
class usesignup(models.Model):
    username=models.CharField(max_length=50)
    firstname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=13)
    number=models.BigIntegerField()
    address=models.TextField()
    pic=models.ImageField(upload_to='media')        

class Category(models.Model):
    category_name =models.CharField(max_length=20)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name

class Policy(models.Model):
    category= models.ForeignKey('Category', on_delete=models.CASCADE)
    policy_name=models.CharField(max_length=200)
    sum_assurance=models.PositiveIntegerField()
    premium=models.PositiveIntegerField()
    tenure=models.PositiveIntegerField()
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.policy_name

class PolicyRecord(models.Model):
    customer= models.ForeignKey(usesignup, on_delete=models.CASCADE)
    Policy= models.ForeignKey(Policy, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,default='Pending')
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.policy

class Question(models.Model):
    customer= models.ForeignKey(usesignup, on_delete=models.CASCADE)
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.description

class questiondata(models.Model):
     description =models.CharField(max_length=500)
     date=models.DateTimeField(auto_now_add=True)
     admin_comment=models.CharField(max_length=200,default='Nothing')