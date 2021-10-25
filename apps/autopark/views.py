from rest_framework.generics import CreateAPIView, ListAPIView

from apps.cars.serializers import CarSerializer

from .models import AutoParkModel
from .serializer import AutoParkSerializer


class AutoParkListView(ListAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkAddCar(CreateAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()

    def perform_create(self, serializer):
        autopark = self.get_object()
        serializer.save(autopark=autopark)


