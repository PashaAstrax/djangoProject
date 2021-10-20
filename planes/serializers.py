from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import PlaneModel

class PlaneSerializer(ModelSerializer):
    class Meta:
        model = PlaneModel
        fields = "__all__"

# class Plane2Serializer(ModelSerializer):
#     class Meta:
#         model = PlaneModel
#         fields = ("id", "brand")

    def validate(self, data):
        if data.get("model") == data.get("brand"):
            raise serializers.ValidationError("Error model is equal brand")
        return data

    def validate_year(self, year):
        if year == 2005:
            raise serializers.ValidationError("Error 2005")
        return year


