from rest_framework import generics
from orderhistory.models import OrderHistory

# Create your views here.
from orderhistory.serializers import OrderHistorySerializer


class OrderList(generics.ListCreateAPIView):
    queryset = OrderHistory.objects.all()

    def get_serializer_class(self):
        return OrderHistorySerializer

    def get_queryset(self):
        if self.kwargs['owner']:
            return OrderHistory.objects.filter(owner=self.kwargs['owner']).order_by('id')
        else:
            return OrderHistory.objects.all()


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderHistory.objects.all()

    def get_serializer_class(self):
        return OrderHistorySerializer

    def get_queryset(self):
        return self.queryset.all()
