from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer

class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        year = self.request.query_params.get("year")
        auto_park = self.request.query_params.get("AutoParkId")
        qs = self.queryset.all()
        if year:
            qs = qs.filter(year__exact=year)
        if auto_park:
            qs = qs.filter(autopark_id=auto_park)
        return qs

class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer