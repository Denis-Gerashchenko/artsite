from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def details(request):
    return render(request, 'details.html', {})


def events(request):
    return render(request, 'events.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})
