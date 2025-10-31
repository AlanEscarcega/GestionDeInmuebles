from django.shortcuts import render

def home(request):
    return render(request, "UrbanStart/home.html")

def contact(request):
    return render(request, "UrbanStart/contact.html")

def about(request):
    return render(request, "UrbanStart/about.html")
