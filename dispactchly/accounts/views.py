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

    def perform_create(self, serializer):
        user = serializer.save()
        
        if user.role == "seller":
            # Check if profile exists
            sender_profile, created = Sender.objects.get_or_create(
                user=user,
                defaults={
                    "business_name": "",
                    "phone_number": "",
                    "pickup_latitude": 0,
                    "pickup_longitude": 0
                }
            )
        elif user.role == "rider":
            rider_profile, created = Rider.objects.get_or_create(
                user=user,
                defaults={
                    "phone_number": "",
                    "vehicle_type": "bike",
                    "availability_status": "offline"
                }
            )


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
    