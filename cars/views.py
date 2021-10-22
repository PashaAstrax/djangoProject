from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer

# class CarListCreateView(APIView):
#
#     def get(self, *args, **kwargs):
#         cars = CarModel.objects.all()
#         serializer = CarSerializer(instance=cars, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
# class CarRetrieveUpdateDestroyView(APIView):
#
#     def get(self, *args, **kwargs):
#         pk = kwargs.get("pk")
#         exists = CarModel.objects.filter(pk=pk).exists()
#         if not exists:
#             return Response("Car with this id is not found", status.HTTP_404_NOT_FOUND)
#         car = CarModel.objects.get(pk=pk)
#         serializer = Car2Serializer(instance=car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs.get("pk")
#         data = self.request.data
#         exists = CarModel.objects.filter(pk=pk).exists()
#         if not exists:
#             return Response("Plane with this id is not found", status.HTTP_404_NOT_FOUND)
#         car = CarModel.objects.get(pk=pk)
#         serializer = CarSerializer(instance=car, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs.get("pk")
#         data = self.request.data
#         exists = CarModel.objects.filter(pk=pk).exists()
#         if not exists:
#             return Response("Car with this id is not found", status.HTTP_404_NOT_FOUND)
#         car = CarModel.objects.get(pk=pk)
#         serializer = CarSerializer(instance=car, data=data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get("pk")
#         exists = CarModel.objects.filter(pk=pk).exists()
#         if not exists:
#             return Response("Car with this id is not found", status.HTTP_404_NOT_FOUND)
#         car = CarModel.objects.get(pk=pk)
#         car.delete()
#         return Response("car deleted", status=status.HTTP_204_NO_CONTENT)

class CarListCreateView(ListCreateAPIView):
    # queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        year = self.request.query_params.get("year")
        auto_park = self.request.query_params.get("AutoParkId")
        qs = CarModel.objects.all()
        if year:
            qs = qs.filter(year__exact=year)
        if auto_park:
            qs = qs.filter(autopark_id=auto_park)
        return qs

    # def get(self, *args, **kwargs):
    #     cars = CarModel.objects.all()
    #     serializer = CarSerializer(instance=cars, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = CarSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_201_CREATED)

class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    # def get(self, *args, **kwargs):
    #     car = self.get_object()
    #     serializer = CarSerializer(instance=car)
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def put(self, *args, **kwargs):
    #     data = self.request.data
    #     car = self.get_object()
    #     serializer = CarSerializer(instance=car, data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def patch(self, *args, **kwargs):
    #     data = self.request.data
    #     car = self.get_object()
    #     serializer = CarSerializer(instance=car, data=data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def delete(self, *args, **kwargs):
    #     car = self.get_object()
    #     car.delete()
    #     return Response("car deleted", status=status.HTTP_204_NO_CONTENT)


