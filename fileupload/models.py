from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
