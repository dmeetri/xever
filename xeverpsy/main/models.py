from django.db import models

class Portfolio(models.Model):
    title = models.TextField()
    description = models.TextField()
    video = models.FileField(upload_to='video/') #file in data base
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
