from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.api.serializers import RegistrationSerializer, ProfileSerializer

User = get_user_model()


class RegistrationCreateAPIView(CreateAPIView):
    """
    post: Create user with username, email, password and confirm password which password should to strong!
    """
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class UserProfileRetrieveAPIView(RetrieveAPIView):
    """
    get: Returns user information entered on the site!
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user
