from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_deadline = models.DateField(null=True, blank=True)
