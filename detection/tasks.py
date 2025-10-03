from celery import shared_task
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib
import os
from django.conf import settings
from .models import UploadDataset, ModelArtifact

@shared_task(bind=True)
def train_model_task(self, dataset_id, params):
    try:
        ds = UploadDataset.objects.get(id=dataset_id)
        ds.status = 'processing'
        ds.save()
        df = pd.read_csv(ds.csv_file.path)

        all_features = list(df.columns)
        numeric_features = list(df.select_dtypes(include=[np.number]).columns)
        dropped_features = [col for col in all_features if col not in numeric_features]

        numeric = df[numeric_features].fillna(0).replace([np.inf, -np.inf], 0)
        scaler = StandardScaler()
        X = scaler.fit_transform(numeric)

        model = IsolationForest(
            n_estimators=params.get('n_estimators', 100),
            contamination=params.get('contamination', 0.01),
            random_state=42
        )
        model.fit(X)

        preds = model.predict(X)  # -1 for anomalies, 1 for normal
        df['anomaly'] = (preds == -1).astype(int)

        artifact = ModelArtifact.objects.create(name=f"isolation_{dataset_id}", params=params)
        model_path = os.path.join(settings.MEDIA_ROOT, 'models', f'{artifact.id}.joblib')
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        joblib.dump({'model': model, 'scaler': scaler}, model_path)
        artifact.file.name = os.path.relpath(model_path, settings.MEDIA_ROOT)
        artifact.metrics = {
            'anomaly_count': int(df['anomaly'].sum()),
            'used_features': numeric_features,
            'dropped_features': dropped_features
        }
        artifact.save()
        ds.status = 'done'
        ds.meta = {'rows': len(df)}
        ds.save()
        return {
            'status': 'success',
            'artifact_id': str(artifact.id),
            'used_features': numeric_features,
            'dropped_features': dropped_features
        }
    except Exception as e:
        ds.status = 'error'
        ds.save()
        raise