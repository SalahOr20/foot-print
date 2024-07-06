
from django.urls import path
from .views import  predict_animal

urlpatterns = [
    path('api/predict-animal/', predict_animal, name='predict-animal'),
]
