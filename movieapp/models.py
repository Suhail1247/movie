from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    imgs=models.ImageField(upload_to='photos')
    def __str__(self):
        return self.name
