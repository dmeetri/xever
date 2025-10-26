from django.db import models
from django.core.validators import FileExtensionValidator

class Portfolio(models.Model):
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    video = models.FileField(
        upload_to='video/',
        null=False,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov'])]
        )
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Services(models.Model):
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    preview = models.ImageField(upload_to='services/', blank=True, null=False)

    def __str__(self) -> str:
        return self.title