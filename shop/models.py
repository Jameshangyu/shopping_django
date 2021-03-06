from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey('shop.Product',on_delete=models.CASCADE,related_name='carts')
    quantity=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product,self.quantity,self.created_date


class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    address=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user,self.address,created_date

    class Meta:
        db_table-'customer'


    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.customer.save()


class LineItem(models.Model):
    quantity=models.IntegerField()
    product=models.ForeignKey('shop.Product',on_delete=models.CASCADE)
    cart=models.ForeignKey('shop.Cart',on_delete=models.CASCADE)
    order=models.ForeignKey('shop.Order',on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quantity,self.product,self.cart,self.order,self.created_date


class Order(models.Model):
    customer=models.ForeignKey('shop.Customer',on_delete=CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer,self.created_date


class Product(models.Model):
    name=models.CharField(max_length=250,db_index=True)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    created_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name,self.price,self.created_date






