from django.conf.urls import include, url
from calculator.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
