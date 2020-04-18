from django.conf.urls import url, include
from .views import all_products, workshop_products, assessory_products, components_products, nutrition_products, clearance_products, product_detail,electronics_products

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^workshop$', workshop_products, name='workshop_products'),
    url(r'^assessory$', assessory_products, name='assessory_products'),
    url(r'^components$', components_products, name='components_products'),
    url(r'^nutrition$', nutrition_products, name='nutrition_products'),
    url(r'^clearance$', clearance_products, name='clearance_products'),
    url(r'^electronics$', electronics_products, name='electronics_products'),
]