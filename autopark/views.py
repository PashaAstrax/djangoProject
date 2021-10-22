from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView

from .models import AutoParkModel
from .serializer import AutoParkSerializer
from cars.serializers import CarSerializer
from cars.models import CarModel

class AutoParkListView(ListAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

class AutoParkAddCar(CreateAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()

    def perform_create(self, serializer):
        autopark = self.get_object()
        serializer.save(autopark=autopark)

class AutoParkRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

# class CarListView(ListAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get_queryset(self):
#         auto_park = self.request.query_params.get("id")
#         qs = CarModel.objects.all()
#         if auto_park:
#             qs = qs.filter(cars__in=auto_park)
#         return qs
