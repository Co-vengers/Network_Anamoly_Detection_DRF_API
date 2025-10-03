from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UploadDataset, ModelArtifact
from .serializers import UploadDatasetSerializer, ModelArtifactSerializer
from .tasks import train_model_task
from rest_framework.views import APIView
from .serializers import RegisterSerializer
import pandas as pd
from .utils import predict_with_artifact

# Create your views here.
class DatasetViewSet(viewsets.ModelViewSet):
    queryset = UploadDataset.objects.all().order_by('-uploaded_at')
    serializer_class = UploadDatasetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class TrainViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def start(self, request):
        dataset_id = request.data.get('dataset_id')
        params = request.data.get('params', {})
        job = train_model_task.delay(dataset_id, params)
        return Response({'job_id': job.id}, status=status.HTTP_202_ACCEPTED)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PredictRunView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            artifact = ModelArtifact.objects.latest('created_at')
        except ModelArtifact.DoesNotExist:
            return Response({"detail": "No trained model found."}, status=404)

        records = request.data.get("records")
        if not records:
            return Response({"detail": "No records provided."}, status=400)

        try:
            df = pd.DataFrame(records)
        except Exception as e:
            return Response({"detail": f"Invalid records format: {e}"}, status=400)

        try:
            preds = predict_with_artifact(artifact, df)
        except Exception as e:
            return Response({"detail": f"Prediction failed: {e}"}, status=500)

        return Response({"predictions": preds.tolist()})