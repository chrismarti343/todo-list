import datetime
from django.utils import timezone

from django.db import models

class Todo(models.Model):
    TodoTitle = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.TodoTitle