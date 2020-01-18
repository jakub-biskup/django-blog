from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        if self.image:
            img = Image.open(self.image.path)

            if img.height > 256 or img.width > 256:
                output_size = (256, 256)
                img.thumbnail(output_size)
                img.save(self.image.path)
