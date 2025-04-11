
from rest_framework import generics
from .models import CustomUser
from .serializers import UserRegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
