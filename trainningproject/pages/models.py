from itertools import product
from os import name
from pyexpat import model
from django.db import models

# Create your models here.


#واحد لواحد 
class Female(models.Model):
    female_name=models.CharField(max_length=50,null=True)
    def __str__(self):
        return  self.female_name



class Male(models.Model):
    male_name=models.CharField(max_length=50,null=True)
    girls=models.OneToOneField(Female,on_delete=models.CASCADE)
    def __str__(self):
        return  self.male_name    

# ############################################################################################################
# واحد لكثير
# علشان هو اللي هيختار كذا منتج user هعمل العلاقه في ال
#  product هنا هعمل المنتجات الاول علشان علشان لو كتبت العكس مش هيفهم ال    

class Product(models.Model):
    title=models.CharField(max_length=50,null=True)
    def __str__(self):
        return  self.title





class User(models.Model):
    name=models.CharField(max_length=50,null=True)
    def __str__(self):
        return  self.name
    products=models.ForeignKey(Product,on_delete=models.CASCADE)




# كثير لكثير 


#  مثال آخر,في حال كنت تبني قاعدة بيانات لجامعة,وتريد تخزين معلومات
# الطلابوالمواد المسجل بها كل طالب.هنا الطالب يمكنه أن يتسجل في عدة
# مواد في نفس الوقت,والمادة الواحدة يمكن أن يتسجل بها عدة طلاب

# زي مثلا الفيديوهات والمشاهده ممكن الفيديو اكتر من واحد يشوفه والواحد يقدر يشوف اكتر من فيديو



class Video(models.Model):
    title=models.CharField(max_length=50,null=True)

    def __str__(self):
        return  self.title

class Username(models.Model):
    name=models.CharField(max_length=50,null=True)
    watch=models.ManyToManyField(Video)

    def __str__(self):
        return  self.name

######################################################## video 30

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
