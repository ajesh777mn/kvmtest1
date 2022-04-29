from django.db import models

# Create your models here.
class home_wallpaper(models.Model):
    wallpaper_text=models.CharField(max_length=150)
    wallpaper_pic=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
   
class tbl_login(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
