from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'vkv-servis/index.html')


def about(request):
    return render(request, 'vkv-servis/about1.html')


def products(request):
    return render(request, 'vkv-servis/products.html')


def contacts(request):
    return render(request, 'vkv-servis/contacts.html')
