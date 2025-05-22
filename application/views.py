from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.throttling import AnonRateThrottle

from account.permissions import IsAttorney

from .models import Application
from .serializers import ApplicationSubmitSerializer, ApplicationListSerializer, ApplicationUpdateSerializer

class ApplicationSubmitView(CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = ApplicationSubmitSerializer
    parser_classes = [MultiPartParser]
    throttle_classes = [AnonRateThrottle]

class ApplicationListView(ListAPIView):
    queryset = Application.objects.all().order_by('-id')
    serializer_class = ApplicationListSerializer
    permission_classes = [IsAuthenticated, IsAttorney]

class ApplicationUpdateView(UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationUpdateSerializer
    permission_classes = [IsAuthenticated, IsAttorney]


