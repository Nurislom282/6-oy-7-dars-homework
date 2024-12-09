from django.urls import path
from .views import main,carmodels,cars,cars_by_models,car_detail


urlpatterns = [
    path('',main,name='home'),
    path('model/<int:model_id>/',cars_by_models,name='car_by_model'),
    path('cars/<int:pk>/', car_detail, name='detail'),
    path('carmodels/',carmodels,name='models'),
    path('cars/',cars,name='car' )
]