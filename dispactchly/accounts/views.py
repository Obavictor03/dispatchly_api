from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Sender, Rider
from .serializers import UserSerializer, UserRegistrationSerializer, SenderSerializer, RiderSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsSender, IsRider


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": f"Welcome to your dashboard, {request.user.name}!",
            "role": request.user.role
        })
    
class SenderDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsSender]

    def get(self, request):
        return Response({
            "message": f"Welcome to the Sender dashboard, {request.user.name}!",
            "role": request.user.role
        })

class RiderDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsRider]

    def get(self, request):
        return Response({
            "message": f"Welcome to the Rider dashboard, {request.user.name}!",
            "role": request.user.role
        })
    