from django.shortcuts import render, get_object_or_404
from .models import ContactMessage, Project, Lecture

def home(request):
    context = {'title': 'Главная страница'}
    return render(request, 'main/home.html', context)

def about(request):
    context = {'title': 'Обо мне'}
    return render(request, 'main/about.html', context)

def portfolio(request):
    projects = Project.objects.all().order_by('-created_at')
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

def lectures(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {
        'title': 'Лекции',
        'lectures': lectures
    }
    return render(request, 'main/lectures.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'title': project.title,
        'project': project
    }
    return render(request, 'main/project_detail.html', context)

def lecture_detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    context = {
        'title': lecture.title,
        'lecture': lecture
    }
    return render(request, 'main/lecture_detail.html', context)
