from django.urls import path

from .views import UserListCreateView, UserRetriveUpdateDestroyView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>', UserRetriveUpdateDestroyView.as_view())
]