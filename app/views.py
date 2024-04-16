from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):

    return render(request,'index.html')


def aboutus(request):
    return render(request,'about-us1.html')



def Pricing(request):
    return render(request,'pricing.html')



def FAQ(request):
    return render(request,'faq.html')


def Sigin(request):
    return render(request,'signin.html')




def Signup(request):
    return render(request,'sign-up.html')




def contact(request):
    return render(request,'contact-us.html')
