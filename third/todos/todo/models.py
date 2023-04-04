from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# models.CASCADE - если пользователь удален, то удалятся все задачи
# models.PROTECTED - запрещает удалять пользователя, пока есть задачи
# models.SET_NULL - задачи остануться в базе, даже при удалении пользователя,
# но значение в поле задачи изменяется на NULL
# models.DEFAULT - задачи остануться в базе, даже при удалении пользователя,
# но значение в поле задачи изменится на значение по умолчанию
