from django.db import models

class Slider(models.Model):
    title = models.CharField(blank=False, null=False)
    description = models.CharField(blank=False, null=False)
    button_text = models.CharField(blank=False, null=False)
    button_link = models.CharField(blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
