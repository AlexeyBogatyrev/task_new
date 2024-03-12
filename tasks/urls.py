"""Определяет схемы URL для learning_logs."""

from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
]
