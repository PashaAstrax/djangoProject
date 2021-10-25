from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer

UserModel: User = get_user_model()

class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    permission_classes = (AllowAny,)


class UserRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
