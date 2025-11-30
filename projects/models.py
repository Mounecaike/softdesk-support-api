from django.db import models
from users.models import User

PROJECT_TYPES = [('BACKEND', 'Backend'),
                 ('IOS', 'Ios'),
                 ('FRONTEND', 'Frontend'),
                 ('ANDROID', 'Android')]

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField(User, through='Contributor', related_name='projects')


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
