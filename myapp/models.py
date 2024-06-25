from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name
class Student(models.Model):
    roll_no = models.IntegerField()
    person = models.ForeignKey(Person,on_delete=models.CASCADE)

'''
create table Product(name varchar,price int, desc varchar)
'''