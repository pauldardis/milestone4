from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def all_products(request):
    """ Displays all products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter().order_by('name')
    paginator = Paginator(product_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})

def product_detail(request, pk):
    """Create a view that returns a single Product object
    based on the post ID (pk) and render it"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {'product': product})






def workshop_products(request):
    """ Displays all workshop products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter().order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})

def assessory_products(request):
    """ Displays assessory products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(catagory="Accessories").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})

def components_products(request):
    """ Displays bike components products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(catagory="Components").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})


def nutrition_products(request):
    """ Displays nutrition products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(catagory="Nutrition").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})


def clearance_products(request):
    """ Displays Clearance products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(catagory="Clearance").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})

def electronics_products(request):
    """ Displays Clearance products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(subcatagory="electronics").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})

def bottles_products(request):
    """ Displays Bottles products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(subcatagory="bottles").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})

def seat_products(request):
    """ Displays Bottles products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(subcatagory="seat").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})

def carrier_products(request):
    """ Displays Bottles products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(subcatagory="carrier").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})

def helmet_products(request):
    """ Displays Bottles products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(subcatagory="helmet").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})

def lights_products(request):
    """ Displays Bottles products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(subcatagory="lights").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})

def locks_products(request):
    """ Displays Bottles products """
    """ Paginate is filtered on product name """
    product_list = Product.objects.filter(subcatagory="locks").order_by('name')
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})