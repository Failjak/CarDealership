from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CreateUserAPIView

urlpatterns = [
    path('create/', CreateUserAPIView.as_view(), name='create'),
    path('login/', TokenObtainPairView.as_view(), name='token_login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
