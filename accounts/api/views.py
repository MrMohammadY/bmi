from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from accounts.api.serializers import RegistrationSerializer

User = get_user_model()


class RegistrationCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
