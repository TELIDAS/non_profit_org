from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from news_npo.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from npo_jwt.serializers import RegisterSerializer, UserDuplicateSerializer
from .serializers import NPOObtainPairSerializer


class NPOObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = NPOObtainPairSerializer



class UserFilterSearch(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDuplicateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['username']
    search_fields = ['=username']
    ordering_fields = ['username']
    ordering = ['username']

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer