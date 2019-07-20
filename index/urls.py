
from django.conf.urls import url
from .views import index, login_view, forget_view

urlpatterns = [
    url(r'^index/$',index),
    url(r'^login/$',login_view),
    url(r'^forget/$',forget_view),
]