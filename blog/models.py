from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User

from user.models import Profile

class Category(models.Model):
    """
    Generic entries so posts can be filtered
    """
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class News_Post(models.Model):
    """
    Inherits Category Model
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    post_img = models.ImageField(default='default.jpg')
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('update_post', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('delete_post', kwargs={
            'pk': self.pk
        })


    def save(self, *args, **kwargs):
        """
        Saves image in 500px x 500px res.
        """
        super(News_Post, self).save(*args, **kwargs)
        img = Image.open(self.post_img.path)
        self.author = User

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.post_img.path)