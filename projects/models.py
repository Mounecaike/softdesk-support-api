from django.db import models
from users.models import User
import uuid


PROJECT_TYPES = [('BACKEND', 'Backend'),
                 ('IOS', 'Ios'),
                 ('FRONTEND', 'Frontend'),
                 ('ANDROID', 'Android')]

# ----- CHOICES -----

ISSUE_TAGS = [
    ('BUG', 'Bug'),
    ('FEATURE', 'Feature'),
    ('TASK', 'Task'),
]

ISSUE_PRIORITY = [
    ('LOW', 'Low'),
    ('MEDIUM', 'Medium'),
    ('HIGH', 'High'),
]

ISSUE_STATUS = [
    ('TODO', 'To Do'),
    ('IN_PROGRESS', 'In Progress'),
    ('DONE', 'Done'),
]


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


class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    tag = models.CharField(max_length=20, choices=ISSUE_TAGS)
    priority = models.CharField(max_length=10, choices=ISSUE_PRIORITY)
    status = models.CharField(max_length=20, choices=ISSUE_STATUS, default='TODO')

    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="issues")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_issues")
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_issues")

    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="comments")

    created_time = models.DateTimeField(auto_now_add=True)