from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart, cart_item_delete, add_to_cart_details

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adddetails/(?P<id>\d+)', add_to_cart_details, name='add_to_cart_details'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    url(r"^delete/(?P<item_id>[0-9]+)/$", cart_item_delete, name="cart_item_delete",),
]