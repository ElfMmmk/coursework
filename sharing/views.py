from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from sharing.models import *
from sharing.permissions import IsAdminOrReadOnly, IsAdminOrAuthenticatedReadOnly
from sharing.serializers import *


# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['author']
    search_fields = ['title', 'excerpt', 'content']
    ordering_fields = ['created_at']


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Vehicle.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['capacity', 'category', 'color', 'brand']
    search_fields = ['name', 'description', 'number']
    ordering_fields = ['mileage', 'price']

    @action(methods=['get'], detail=False)
    def empty(self, request):
        drives = Drive.objects.filter(status=Drive.ACTIVE).values_list('vehicle_id', flat=True)
        vehicles = Vehicle.objects.exclude(id__in=drives)

        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)


class BikeViewSet(viewsets.ModelViewSet):
    serializer_class = BikeSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Bike.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['category', 'color', 'brand']
    search_fields = ['name', 'description']
    ordering_fields = ['price']

    @action(methods=['get'], detail=False)
    def empty(self, request):
        drives = Drive.objects.exclude(status=Drive.ACTIVE).values_list('bike_id', flat=True)
        bikes = Bike.objects.filter(id__in=drives)

        serializer = BikeSerializer(bikes, many=True)
        return Response(serializer.data)


class DriveViewSet(viewsets.ModelViewSet):
    serializer_class = DriveSerializer

    queryset = Drive.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['tariff', 'vehicle', 'bike', 'status']
    ordering_fields = ['total', 'date', 'duration', 'rating']

    @action(methods=['post'], detail=True)
    def stop(self, request, pk=None):
        drive = self.get_object()
        print('drive')
        if drive.status == Drive.FINISHED:
            return Response(serializers.ErrorDetail('Данная поездка уже завершена.'))

        drive.status = Drive.FINISHED

        rating = request.POST['rating']
        if not rating:
            return Response(serializers.ValidationError('Rating requirement!'))

        drive.rating = rating
        drive.save()

        serializer = DriveSerializer(drive)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def current_in_vehicle(self, request):
        drives = Drive.objects.filter(Q(status=Drive.ACTIVE) & Q(vehicle__isnull=False))

        serializer = DriveSerializer(drives, many=True)
        return Response(serializer.data)


class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = (IsAdminUser,)
    queryset = Feedback.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['email', 'subject']
    ordering_fields = ['date']


class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Color.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']


class ProducerViewSet(viewsets.ModelViewSet):
    serializer_class = ProducerSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Producer.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
