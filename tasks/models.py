from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    HIGHT = "Высокий"
    MEDIUM = "Средний"
    LOW = "Низкий"

    priority = {
        HIGHT: "Высокий",
        MEDIUM: "Средний",
        LOW: "Низкий",
    }

    title = models.CharField(max_length=200)
    text = models.CharField(max_length=400)
    priority = models.CharField(max_length=200, choices=priority.items())
    state = models.BooleanField(default=False)
    date_finish = models.DateField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.title
