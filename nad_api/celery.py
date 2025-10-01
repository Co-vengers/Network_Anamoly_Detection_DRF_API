import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nad_api.settings')  # <-- fix here
app = Celery('nad_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()