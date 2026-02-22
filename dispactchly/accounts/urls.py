from django.urls import path
from .views import RegisterView, UserDashboardView, SenderDashboardView, RiderDashboardView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserDashboardView.as_view(), name='user'),
    path('sender/', SenderDashboardView.as_view(), name='sender'),
    path('rider/', RiderDashboardView.as_view(), name='rider'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]