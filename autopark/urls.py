from django.urls import path

from .views import AutoParkListView, AutoParkAddCar

urlpatterns = [
    path('', AutoParkListView.as_view()),
    path('/<int:pk>/add_car', AutoParkAddCar.as_view())
]