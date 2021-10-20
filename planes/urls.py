from django.urls import path

from .views import PlaneListCreateView, PlaneRetrieveUpdateDestroyView

urlpatterns = [
    path('', PlaneListCreateView.as_view()),
    path('/<int:pk>', PlaneRetrieveUpdateDestroyView.as_view())
]
# http://localhost:8000/