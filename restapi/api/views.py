from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from api.models import User, UserProfile
from api.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from .serializers import RegisterSerializer
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def get_permissions(self):
    if self.action == 'create':
        permission_classes = [AllowAny]
    elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
        permission_classes = [IsLoggedInUserOrAdmin]
    elif self.action == 'list' or self.action == 'destroy':
        self.permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]
