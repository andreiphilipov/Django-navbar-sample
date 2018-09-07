from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    from pages.name import name
    # my_name = "Hello, My name is Andrei"
    return render(request, 'about.html', {"john": name})

def contact(request):
    return render(request, 'contact.html', {})