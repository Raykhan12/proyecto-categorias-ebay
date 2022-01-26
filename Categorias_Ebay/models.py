from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Category(models.Model):
    BestOfferEnabled=models.BooleanField(default=True,null=True,blank=True) 
    AutoPayEnabled=models.BooleanField(default=True,null=True,blank=True)
    CategoryID=models.PositiveIntegerField(primary_key=True)
    CategoryLevel=models.PositiveSmallIntegerField()
    CategoryName=models.TextField(max_length=100,null=True,blank=True)
    CategoryParentID=models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True)
    LeafCategory=models.BooleanField(null=True,blank=True)   
    
      
    