from rest_framework import serializers
from .models import UploadDataset, ModelArtifact

class UploadDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadDataset
        fields = '__all__'
        read_only_fields = ('id', 'uploaded_at', 'status', 'meta')

class ModelArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelArtifact
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'metrics')