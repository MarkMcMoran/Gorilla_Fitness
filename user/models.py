from PIL import Image
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Profile(models.Model):
    """
    Profile model, this allows users to modify their profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    about = models.TextField(max_length=150, blank=True)
    goals = models.TextField(max_length=100, blank=True)
    reason_join = models.TextField(max_length=100, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        try:
            return f"{self.user}"
        except ObjectDoesNotExist:
            return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
        Saves image in 300px x 300px res.
        """

        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
