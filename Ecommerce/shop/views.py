from django.shortcuts import render
from django.http import HttpResponse

# def all_user(request):
#     return HttpResponse("this is my out put")

def home(request):
    return render(request,'shop/index.html')
def house(request):
    return render(request,'shop1/index2.html')
def register(request):
    return render(request,'shop/register.html')
