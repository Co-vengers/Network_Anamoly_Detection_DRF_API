from django.db import models

import uuid

# Create your models here.
def model_upload_path(instance, filename):
    return f"models/{instance.id}/filename"

class UploadDataset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uploaded_by = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)
    csv_file = models.FileField(upload_to='Datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, default='uploaded')
    meta = models.JSONField(null=True, blank=True)

class ModelArtifact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=model_upload_path)
    metrics = models.JSONField(null=True, blank=True)
    params = models.JSONField(null=True, blank=True)
