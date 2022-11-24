import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @admin.display(
        boolean=True,
        ordering='created',
        description='Publicado recientemente?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created <= now

    # @admin.display(
    #     boolean=True,
    #     ordering='user',
    #     description='Publicado por',
    # )
    def created_by(self):
        return self.user.username
