from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Project, Lecture, Feedback, Subscriber
from .forms import FeedbackForm, SubscriptionForm, UnsubscribeForm

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
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено! Мы ответим вам в ближайшее время.')
            return redirect('contacts')
    else:
        form = FeedbackForm()
    context = {
        'title': 'Контакты',
        'form': form
    }
    return render(request, 'main/contacts.html', context)

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

def feedback_list(request):
    if not request.user.is_staff:
        return redirect('home')
    feedbacks = Feedback.objects.all()
    context = {
        'title': 'Сообщения обратной связи',
        'feedbacks': feedbacks
    }
    return render(request, 'main/feedback_list.html', context)

def subscribers_list(request):
    if not request.user.is_staff:
        return redirect('home')
    subscribers = Subscriber.objects.all()
    context = {
        'title': 'Подписчики',
        'subscribers': subscribers
    }
    return render(request, 'main/subscribers_list.html', context)
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscriber = Subscriber.objects.filter(email__iexact=email).first()
            if subscriber:
                if subscriber.is_active:
                    form.add_error('email', 'Вы уже подписаны')
                else:
                    subscriber.is_active = True
                    subscriber.subscribed_at = timezone.now()
                    subscriber.save()
                    return redirect('subscribe_success')
            else:
                Subscriber.objects.create(email=email, is_active=True)
                return redirect('subscribe_success')
    else:
        form = SubscriptionForm()
    context = {'title': 'Подписка', 'form': form}
    return render(request, 'main/subscribe.html', context)

def subscribe_success(request):
    context = {'title': 'Подписка оформлена'}
    return render(request, 'main/subscribe_success.html', context)

def unsubscribe(request):
    if request.method == 'POST':
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscriber = Subscriber.objects.filter(email__iexact=email, is_active=True).first()
            if subscriber:
                subscriber.is_active = False
                subscriber.save()
                return render(request, 'main/unsubscribe.html', {'title': 'Отписка', 'form': UnsubscribeForm(), 'unsubscribed': True})
            else:
                form.add_error('email', 'Подписка не найдена')
    else:
        form = UnsubscribeForm()
    context = {'title': 'Отписка', 'form': form}
    return render(request, 'main/unsubscribe.html', context)
