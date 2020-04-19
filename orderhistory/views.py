from rest_framework import generics
from orderhistory.models import OrderHistory

# Create your views here.
from orderhistory.serializers import OrderHistorySerializer


class OrderList(generics.ListCreateAPIView):
    queryset = OrderHistory.objects.all()

    def get_serializer_class(self):
        return OrderHistorySerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderHistory.objects.all()

    def get_serializer_class(self):
        return OrderHistorySerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.owner)
