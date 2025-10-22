from django.db import models
import os

class PostVideo(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название видео"
    )
    video_file = models.FileField(
        upload_to='videos/',
        verbose_name="Видео файл"
    )
    def __str__(self):
        return self.title
    
    def filename(self):
        return os.path.basename(self.video_file.name)

# Create your models here.
