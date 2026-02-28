from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Delivery
from .serializers import DeliverySerializer
from accounts.models import Sender, Rider
from accounts.permissions import IsSender,IsRider

# Create your views here.

# Sender's Endpoint
class CreateDeliveryView(APIView):
    permission_classes = [IsAuthenticated, IsSender]

    def post(self, request):
        sender = Sender.objects.get(user=request.user)
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=sender)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class MyDeliveriesView(APIView):
    permission_classes = [IsAuthenticated, IsSender]
    
    def get(self, request):
        sender = Sender.objects.get(user=request.user)
        deliveries = Delivery.objects.filter(sender=sender).order_by('-created_at')
        serializer = DeliverySerializer(deliveries, many=True)
        return Response(serializer.data)
    

class DeleveryDetailView(APIView):
    permission_classes = [IsAuthenticated, IsSender]

    def get(self, pk, request):
        sender = Sender.objects.get(user=request.user)

        try:
            delivery = Delivery.objects.get(id=pk, sender=sender)
        except Delivery.DoesNotExist:
            return Response({'error': 'Delivery not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DeliverySerializer(delivery)
        return Response(serializer.data)
    

class CancelDeliveryView(APIView):
    permission_classes = [IsAuthenticated, IsSender]

    def delete(self, request, pk):
        sender = Sender.objects.get(user=request.user)

        try:
            delivery =  Delivery.objects.get(id=pk, sneder=sender)
        except Delivery.DoesNotExist:
            return Response({'error': 'Delivery not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if delivery.status != 'pending':
            return Response({'error': 'Cannot cancel after rider has accepted'}, status=400)
        delivery.status = 'cancelled'
        delivery.save()

        return Response({'message': 'Delivery cancelled succesfully'})
    


# Rider's Endpoint
class AvailableDeliveriesView(APIView):
    permission_classes = [IsAuthenticated, IsRider]

    def get(self, request):
        deliveries = Delivery.objects.filter(status='pending', rider__isnull = True).order_by('-created_at')
        serializer = DeliverySerializer(deliveries, many=True)
        return Response(serializer.data)
    

class AcceptDeliveryView(APIView):
    permission_classes = [IsAuthenticated, IsRider]

    def post(self, request, pk):
        rider = Rider.objects.get(user=request.user)
        try:
            delivery = Delivery.objects.get(id=pk)
        except Delivery.DoesNotExist:
            return Response({'error': 'Delivery not found'}, status=404)
        
        if delivery.status != 'pending':
            return Response({'error': 'Delivery not available'}, status=400)
        delivery.rider = rider
        delivery.status = 'accepted'
        delivery.save()

        return Response({'message': 'Delvery accepted'})
    


class RiderDeliveryView(APIView):
    permission_classes = [IsAuthenticated, IsRider]

    def get(self, request):
        rider = Rider.objects.get(user=request.user)
        deliveries = Delivery.objects.filter(rider=rider).order_by('-created_at')
        serializer = DeliverySerializer(deliveries, many=True)
        return Response(serializer.data)
    

class UpdateDeliveryStatusView(APIView):
    permission_classes = [IsAuthenticated, IsRider]

    def patch(self, request, pk):
        rider = Rider.objects.get(user=request.user)
        try:
            delivery = Delivery.objects.filter(id=pk, rider=rider)
        except Delivery.DoesNotExist:
            return Response({'error': 'Delivery not found'}, status=404)
        
        new_status = request.data.get('status')
        allowed = ['picked_up', "in_transit", 'delivered']

        if new_status not in allowed:
            return Response({'error': "Invalid status"}, status=400)
        
        delivery.status = new_status
        delivery.save()

        return Response({'message': 'Status updated'})
    


class UpdateAvailabilityView(APIView):
    permission_classes = [IsAuthenticated, IsRider]

    def patch(self, request):
        rider = Rider.objects.get(user=request.user)

        new_status = request.data.get('availability_status')
        allowed = ['available', 'busy', 'offline']

        if new_status not in allowed:
            return Response({'error': 'Invalid status'}, status=400)
        
        rider.availability_status = new_status
        rider.save()

        return Response ({'message': 'Availability Updated'})