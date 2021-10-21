from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PlaneModel
from .serializers import PlaneSerializer

class PlaneListCreateView(APIView):

    def get(self, *args, **kwargs):
        # planes = PlaneModel.objects.filter(year__gte=2019).order_by("brand").exclude(year=2020)
        # planes = planes.objects.filter(year__gte=2020).order_by("brand")[1:]
        planes = PlaneModel.objects.all()
        year = self.request.query_params.get("year")
        if year:
            planes = planes.filter(year__exact=year)
        serializer = PlaneSerializer(instance=planes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = PlaneSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class PlaneRetrieveUpdateDestroyView(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        exists = PlaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response("Plane with this id is not found", status.HTTP_404_NOT_FOUND)
        plane = PlaneModel.objects.get(pk=pk)
        serializer = PlaneSerializer(instance=plane)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get("pk")
        data = self.request.data
        exists = PlaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response("Plane with this id is not found", status.HTTP_404_NOT_FOUND)
        plane = PlaneModel.objects.get(pk=pk)
        serializer = PlaneSerializer(instance=plane, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get("pk")
        data = self.request.data
        exists = PlaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response("Plane with this id is not found", status.HTTP_404_NOT_FOUND)
        plane = PlaneModel.objects.get(pk=pk)
        serializer = PlaneSerializer(instance=plane, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get("pk")
        exists = PlaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response("Plane with this id is not found", status.HTTP_404_NOT_FOUND)
        plane = PlaneModel.objects.get(pk=pk)
        plane.delete()
        return Response("Plane deleted", status=status.HTTP_204_NO_CONTENT)


