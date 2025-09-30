import joblib
from django.conf import settings
from .models import ModelArtifact
import os

def load_artifact(artifact: ModelArtifact):
    path = os.path.join(settings.MEDIA_ROOT, artifact.file.name)
    return joblib.load(path)

def predict_with_artifact(artifact, df_record):
    obj = load_artifact(artifact)
    scaler = obj['scaler']
    model = obj['model']
    X = scaler.transform(df_record)
    preds = model.predict(X)
    return preds
