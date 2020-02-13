from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })


class Drawing(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(null=True, blank=True)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.TextField()
    sold = models.BooleanField(null=True)
    price = models.TextField()
    shops = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })


class ImageModel(models.Model):
    mainimage = models.ImageField(upload_to='img', null=True)
    image = models.ForeignKey(Drawing, on_delete=models.CASCADE)