from django.db import models
from django.conf import settings

class Trip(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    source= models.CharField(max_length=255)
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.PositiveIntegerField()
    currency = models.CharField(max_length=100)
    interests = models.TextField(help_text="Comma-separated interests like food, history, adventure")
    created_at = models.DateTimeField(auto_now_add=True)
