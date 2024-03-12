from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'text', 'priority', 'state', 'date_finish']
        labels = {'title': 'Заголовок', 'text': 'Описание', 'priority': 'Приоритет', 'state': 'Статус', 'date_finish': 'Дата выполнения'}
