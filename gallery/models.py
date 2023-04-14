from django.db import models

# Create your models here.

class Photo(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    captions = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Gallery(models.Model):
    name = models.CharField(max_length=250)
    images = models.ManyToManyField(Photo)
    captions = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']