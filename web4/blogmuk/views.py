# views of blogmuk
from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    return HttpResponse("This is the blog page.")
def firtpage(request):
    return HttpResponse("firtpage")



