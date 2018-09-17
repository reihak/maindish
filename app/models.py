from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=150)
    food_stuff = models.TextField(blank=True)
    name = models.TextField(blank=True)
    link = models.TextField(blank=True)
    text = models.TextField(blank=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
