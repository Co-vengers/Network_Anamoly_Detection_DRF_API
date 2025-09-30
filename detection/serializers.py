from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UploadDataset, ModelArtifact

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

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