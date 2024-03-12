from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic
from .forms import TopicForm

# Create your views here.


def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'tasks/index.html')


@login_required
def topics(request):
    """Выводит список тем."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'tasks/topics.html', context)


@login_required
def new_topic(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('tasks:topics')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'tasks/new_topic.html', context)


@login_required
def edit_topic(request, topic_id):
    """Редактирует существующую запись."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = TopicForm(instance=topic)
    else:
        # Отправка данных POST; обработать данные.
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:topics')
    context = {'topic': topic, 'form': form}
    return render(request, 'tasks/edit_topic.html', context)
