from django.shortcuts import render
from .models import ContactMessage

def home(request):
    context = {'title': 'Главная страница'}
    return render(request, 'main/home.html', context)

def about(request):
    context = {'title': 'Обо мне'}
    return render(request, 'main/about.html', context)

def portfolio(request):
    projects = ["Проект 1", "Проект 2", "Проект 3"]
    context = {
        'title': 'Портфолио', 
        'projects': projects
    }
    return render(request, 'main/portfolio.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            return render(request, 'main/contacts.html', {'title': 'Контакты', 'submitted': True})
    return render(request, 'main/contacts.html', {'title': 'Контакты'})
