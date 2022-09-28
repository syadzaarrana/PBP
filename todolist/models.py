from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    is_finished = models.BooleanField(default=False)

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user', 'is_finished']