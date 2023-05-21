from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # 5MB

    if image.size > max_size:
        raise ValidationError(f"The image size should not exceed 5MB.")


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    picture = models.ImageField(upload_to="img", default="", validators=[validate_image_size], blank=True)
    quantity = models.IntegerField(default=1)
    
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems]) # in this way we are loading data on memory but or test we can use it
        return total
    
    
      
    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product.name
    
    @property
    def price(self):
        new_price = self.product.price * self.quantity
        return new_price
  
        
    
    