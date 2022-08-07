from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.


class Products(models.Model):
    name=models.CharField(max_length=20)
    content=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    # image=models.ImageField(upload_to='photos/%y/%m/%d')
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class  Meta:
        verbose_name = 'phone'
        ordering=['-price']
        

