from django.db import models

# Create your models here.

class Url(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10)
    visits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_url