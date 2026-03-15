from django.urls import path
from .views import (CancelDeliveryView, CreateDeliveryView, MyDeliveriesView, DeleveryDetailView, RiderDeliveryView, AcceptDeliveryView, UpdateAvailabilityView, AvailableDeliveriesView, UpdateDeliveryStatusView)

urlpatterns = [
    path('', CreateDeliveryView.as_view()),
    path('my/', MyDeliveriesView.as_view()),
    path('<int:pk>/', DeleveryDetailView.as_view()),
    path('<int:pk>/cancel', CancelDeliveryView.as_view()),
    path('available/', AvailableDeliveriesView.as_view()),
    path('<int:pk>/accept/', AcceptDeliveryView.as_view()),
    path('<int:pk>/status/', UpdateDeliveryStatusView.as_view()),
    path('rider/my-deliveries/', RiderDeliveryView.as_view()),
    path('rider/availability/', UpdateAvailabilityView.as_view()),
]