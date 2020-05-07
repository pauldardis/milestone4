from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.utils.html import format_html

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    message = format_html(
        'Item added to your cart. ')
    messages.success(
        request, message)
    return redirect(reverse('shop'))



def add_to_cart_details(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    message = format_html(
        'Item added to your cart. ')
    messages.success(
        request, message)
    return redirect(reverse('product_detail', args=(id,)))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    message = format_html(
        'Your cart has been updated ')
    messages.success(
        request, message)

    return redirect(reverse('view_cart'))


def cart_item_delete(request, item_id):

    """
    User will be able to remove selected items from the shopping
    cart. This option is availible in the cart view
    """
    cart = request.session.get('cart', {})

    if request.method == "POST":            
        if cart and cart.get(item_id):
            cart.pop(item_id)
            request.session["cart"] = cart
    message = format_html(
        'The item has been deleted ')
    messages.success(
        request, message)

    return redirect(reverse("view_cart"))
        