from django.shortcuts import render
from .models import Product, Cart, CartItem
from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from store.validations import check_out_of_stock
# Create your views here.

@login_required(login_url='/admin')
def index(request):
    products = Product.objects.all()
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        request.session['cart_id'] = str(cart.id)
    context = {"products":products, "cart": cart}
    return render(request, "index.html", context)


def cart(request):
    
    cart = None
    cartitems = []
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
    
    context = {"cart":cart, "items":cartitems}
    return render(request, "cart.html", context)



def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    qty = data["qty"]
    product = Product.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        check_stock = check_out_of_stock(product, qty)
        if not check_stock:
            cartitem, created =CartItem.objects.get_or_create(cart=cart, product=product)
            cartitem.quantity = int(qty)
            product.quantity -= int(qty)
            product.save()
            cartitem.save()
        else:
            num_of_item = cart.num_of_items
            data = {
                'num_of_item':num_of_item,
                'error':check_stock

            }
            return JsonResponse(data, safe=False)
        
        
        num_of_item = cart.num_of_items
        
    return JsonResponse({'num_of_item':num_of_item}, safe=False)



def payment_complete(cart_id):
    update_cart = Cart.objects.filter(id=cart_id).update(completed=True)
    if update_cart:
        return True
    return False
    

def update_cart(request):
    data = json.loads(request.body)
    get_cart_id = request.session['cart_id']
    

    if data['type'] == 'payment_confirm':
        if payment_complete(get_cart_id):
            messages.success(request, "Payment made successfully")
            return JsonResponse({'data':'done'}, safe=False)
        messages.success(request, "Payment made not successfull")
        return JsonResponse({'data':'error'}, safe=False)
    

    elif data['type'] == 'qty':

        qty = data['qty']
        product = Product.objects.get(id=data['product_id'])
        cart = Cart.objects.get(user=request.user, completed=False)
        check_stock = check_out_of_stock(product, int(qty))
        cartitem = CartItem.objects.get(cart=cart, product=product)
        if not check_stock:
            cartitem.quantity = int(qty)
            product.quantity -= int(qty)
            product.save()
            cartitem.save()
            num_of_item = cart.num_of_items
            data = {
                'num_of_item':num_of_item,
                'error':check_stock,
                'total_price':cart.total_price,
                'price': cartitem.price

            }
            return JsonResponse(data, safe=False)
        else:
            num_of_item = cart.num_of_items
            data = {
                'num_of_item':num_of_item,
                'error':check_stock,
                'total_price':cart.total_price,
                'price': cartitem.price

            }
            return JsonResponse(data, safe=False)
        
        
