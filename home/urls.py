from django.conf.urls import url
from .views import home, about, contact, spare, send_email, contact_success

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^spare/$', spare, name='spare'),
    url(r'^send/', send_email, name='send_email'),
    url(r'^contact_success/$', contact_success, name='contact_success'),



]