from django.db import models

# Create your models here.

class Mesta(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # photo = models.ImageField(upload_to="photo/%Y/%m/%d/")