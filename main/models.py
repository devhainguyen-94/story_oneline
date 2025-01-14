from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.conf import settings
class Role(models.Model):
    name = models.TextField()
    # created_by = models.ForeignKey(User, related_name='cre', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']
class CustomUser(AbstractUser):
    # Add custom fields here, if needed
    ROLES = [
        ('admin', 'Administrator'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    ]

    # role = models.ForeignKey(Role, related_name='role', on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20, choices=ROLES, default=ROLES[0][0])
    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
class Book(models.Model):
    title = models.CharField(max_length=200)
    auth =  models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/books/')
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
class Chapter(models.Model):
    number_chapter = models.IntegerField(default=0)
    content = models.TextField()
    image = models.ImageField(upload_to='images/chapter/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)