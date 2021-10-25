from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

from apps.profile.serializers import ProfileSerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer

    class Meta:
        model = UserModel
        fields = (
            "id", "email", "password", "is_superuser", "is_staff", "is_active", "last_login", "created_at", "updated_at", "profile"
        )
        extra_kwargs = {
            "password": {"write_only": True}
        }