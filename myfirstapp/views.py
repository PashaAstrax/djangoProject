from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ComputerModel

class ComputerListCreateView(APIView):

    def get(self, *args, **kwargs):
        comps = ComputerModel.objects.all().values()
        return Response(comps, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        comp = ComputerModel.objects.create(**data)
        return Response(model_to_dict(comp), status.HTTP_201_CREATED)

class ComputerRetrieveUpdateDestroyView(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response("Computer with this id is not found", status.HTTP_404_NOT_FOUND)
        comp = ComputerModel.objects.get(pk=pk)
        return Response(model_to_dict(comp), status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get("pk")
        data = self.request.data
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response("Computer with this id is not found", status.HTTP_404_NOT_FOUND)
        ComputerModel.objects.filter(pk=pk).update(**data)
        return Response("Computer update", status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get("pk")
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response("Computer with this id is not found", status.HTTP_404_NOT_FOUND)
        comp = ComputerModel.objects.get(pk=pk)
        comp.delete()
        return Response("Computer deleted", status=status.HTTP_204_NO_CONTENT)


