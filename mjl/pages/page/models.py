from django.db import models
class douban(models.Model):
    name=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    intro=models.CharField(max_length=255)
    date=models.CharField(max_length=255)  
    price=models.CharField(max_length=255)
    Press=models.CharField(max_length=255)
    point=models.CharField(max_length=255)
class jingdong(models.Model):
    ititle=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    intro=models.CharField(max_length=255)
class tianqiyubao(models.Model):
    city=models.CharField(max_length=255)  
    date=models.CharField(max_length=255)
    weather=models.CharField(max_length=255)
    temp=models.CharField(max_length=255)