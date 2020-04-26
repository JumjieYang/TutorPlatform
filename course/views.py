from course.models import Course, ShoppingCart
from course.serializers import CourseSerializer, CartSerializer
from rest_framework import generics


class CourseCreateView(generics.CreateAPIView):
    def get_serializer_class(self):
        return CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_authenticators(self):
        return ()

    def get_permissions(self):
        return ()

    def get_queryset(self):
        queryset = Course.objects.all()

        tutorId = self.request.query_params.get('tutor', None)
        if tutorId is not None:
            return queryset.filter(tutor=tutorId)
        return queryset


class CartList(generics.ListCreateAPIView):
    queryset = ShoppingCart.objects.all()

    def get_serializer_class(self):
        return CartSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingCart.objects.all()

    def get_serializer_class(self):
        return CartSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
