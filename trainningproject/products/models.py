from datetime import datetime
from distutils.command.upload import upload
from email.mime import image
from unicodedata import category
from django.db import models

# Create your models here.

class Products(models.Model):

    # x=[
    #     ('phones','phones')
    #     ('computer','computer')   
    # ]

    name=models.CharField(max_length=20,default='type the name')
    content=models.TextField(default='content',null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='photos/%y/%m/%d',blank=True,verbose_name='photos')
    active=models.BooleanField(default=True)
    # category=models.CharField(max_length=20,choices=x)

    def __str__(self):
        return self.name

    class  Meta:
        verbose_name = 'phone'
        # ordering=['-price']
        





class Test(models.Model):
    date=models.DateField()
    time=models.TimeField(null=True)
    created= models.DateTimeField(default=datetime.now)


