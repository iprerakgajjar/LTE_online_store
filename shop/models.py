from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    product_desc=models.CharField(max_length=400)
    product_date=models.DateField()
    product_img=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    con_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80, default="")
    phone = models.CharField(max_length=80, default="")
    feedback = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.name
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=2000)
    fname=models.CharField(max_length=500)
    lname=models.CharField(max_length=500)
    email=models.CharField(max_length=800,default="")
    address1=models.CharField(max_length=800,default="")
    address2=models.CharField(max_length=800,default="")
    phone=models.CharField(max_length=800,default="")
    state=models.CharField(max_length=500)
    city=models.CharField(max_length=500,default="")
    zip=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.fname




