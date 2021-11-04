from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

# Create your models here.


#1. One to One Model Relation

class User(models.Model):
    name = models.CharField(max_length=100)


class Email(models.Model):
    email = models.EmailField(max_length=100, default=None)


class Address(models.Model):
    street = models.CharField(max_length=100)

class Caste(models.Model):
    caste = models.CharField(max_length=100)

class Province(models.Model):
    province = models.CharField(max_length=100)

# Many-to-Many Relation
class Country(models.Model):
    name = models.CharField(max_length=100)

class UserDetail(models.Model):
    age = models.IntegerField()
    # Inherting the User Class Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.OneToOneField(Email, on_delete=models.CASCADE)
    # address may be same for more than one user
    # so we have maintained Foreign key here
    address = models.ForeignKey(Address,
                                # Let's add a related_name
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='user_addresses')
    
    # another foreign modelrelation as Caste
    caste = models.ForeignKey(Caste,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name='user_caste')
    
    # province field as foreign model relation
    province = models.ForeignKey(Province,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='user_province')
    
    #many to many relation type
    country = models.ManyToManyField(Country)


