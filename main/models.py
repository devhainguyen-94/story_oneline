from django.db import models
from django.utils import timezone
class Role(models.Model):
    name = models.TextField()
    role_name = models.TextField()
    created_by = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']
class Category(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
class Book(models.Model):
    title = models.CharField(max_length=200)
    # auth =  models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField()
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
class Chapter(models.Model):
    number_chapter = models.IntegerField(default=0)
    content = models.TextField()
    image = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)