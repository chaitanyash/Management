from django.conf.urls import url,include
from . import views
from .views import *

urlpatterns = [
    url(r'^department/$', departmentApi),
    url(r'^course/$', courseApi),
    url(r'^parent/$', parentApi),
]