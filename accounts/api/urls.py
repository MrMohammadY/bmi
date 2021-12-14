from django.urls import path

from accounts.api.views import RegistrationCreateAPIView

app_name = 'api'

urlpatterns = [
    path('registration/', RegistrationCreateAPIView.as_view(), name='registration'),
]
