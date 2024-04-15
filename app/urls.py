from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index-page"),
    path('aboutus/',aboutus,name="about-page")
]



