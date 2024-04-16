from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index-page"),
    path('aboutus/',aboutus,name="about-page"),
    path('pricing/',Pricing,name="pricing-page"),
    path('faq/',FAQ,name="faq-page"),
    path('signin/',Sigin,name="signin-page"),
    path('signup/',Signup,name="signup-page")
]




