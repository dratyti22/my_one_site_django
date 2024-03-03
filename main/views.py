from django.shortcuts import render

from .models import Index, About, Contact


def index(request):

    content = Index.objects.all()
 
    context = {
        'title': 'Home - Главная',
        'content': content
    }
    return render(request, 'main/index.html', context)


def about(request):
    text = About.objects.all()

    context = {
        'title': 'Home - О нас',
        'content': text
    }

    return render(request, 'main/about.html', context)


def contact(request):
    content = Contact.objects.all()

    context = {
        'title': 'Home - Контакты',
        'content': content
    }
    return render(request, 'main/contact.html', context)
