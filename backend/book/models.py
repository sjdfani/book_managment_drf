from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BookModel(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    pages = models.PositiveIntegerField(default=0)
    picture = models.ImageField()

    class Meta:
        verbose_name = 'Book'
    
    def __str__(self):
        return self.name
