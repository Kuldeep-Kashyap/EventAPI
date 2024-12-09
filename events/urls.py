from django.urls import path
from .views import RegisterView, EventView, purchase_ticket
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('events/', EventView.as_view(), name='events'),
    path('events/<int:id>/purchase/', purchase_ticket, name='purchase_ticket'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
