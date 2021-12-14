from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from accounts.api.views import RegistrationCreateAPIView, UserProfileRetrieveAPIView

app_name = 'api'

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', RegistrationCreateAPIView.as_view(), name='registration'),
    path('profile/', UserProfileRetrieveAPIView.as_view(), name='profile'),
]
