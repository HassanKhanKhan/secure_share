from django.conf import settings
from django.db import models

class SecureFile(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='secure_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    size = models.BigIntegerField()

    def __str__(self):
        return self.file.name



