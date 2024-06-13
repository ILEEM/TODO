from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    PRIORITY_CHOICES = [('H','High'),('M','Medium'),('L','Low')]
    Task = models.CharField(max_length=50)
    Description = models.TextField()
    Priority = models.CharField(max_length=1,choices=PRIORITY_CHOICES)
    DateTime = models.DateTimeField(default=timezone.now)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Task