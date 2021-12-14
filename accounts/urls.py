from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from accounts.views import UserRegistrationView, UserLoginView, UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('accounts:login')), name='logout'),
]
