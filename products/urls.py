from django.conf.urls import url, include
from .views import all_products, workshop_products, assessory_products
from .views import components_products, nutrition_products, clearance_products
from .views import product_detail,electronics_products, bottles_products, seat_products
from .views import  carrier_products, helmet_products, lights_products, locks_products







urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^workshop$', workshop_products, name='workshop_products'),
    url(r'^assessory$', assessory_products, name='assessory_products'),
    url(r'^components$', components_products, name='components_products'),
    url(r'^nutrition$', nutrition_products, name='nutrition_products'),
    url(r'^clearance$', clearance_products, name='clearance_products'),
    url(r'^electronics$', electronics_products, name='electronics_products'),
    url(r'^bottles_products', bottles_products, name='bottles_products'),
    url(r'^seat$', seat_products, name='seat_products'),
    url(r'^carrier$', carrier_products, name='carrier_products'),
    url(r'^helmets$', helmet_products, name='helmet_products'),
    url(r'^lights$', lights_products, name='lights_products'),
    url(r'^locks$', locks_products, name='locks_products'),
]