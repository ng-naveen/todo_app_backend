from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
        ('critical', 'critical')
    ]

    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('in-progress', 'in-progress'),
        ('completed', 'completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateField(auto_now_add=True)
    completed_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
