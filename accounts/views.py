from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView, TemplateView

from accounts.forms import RegistrationForm, LoginForm


@method_decorator(require_http_methods(['POST', 'GET']), name='dispatch')
class UserRegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('accounts:registration')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.password = make_password(instance.password)
        instance.save()
        messages.info(self.request, 'Registration Success', 'success')
        return super().form_valid(form)


@method_decorator(require_http_methods(['POST', 'GET']), name='dispatch')
class UserLoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        user = form.cleaned_data['user']
        if user:
            login(self.request, user)
        return super().form_valid(form)


@method_decorator(require_http_methods(['GET']), name='dispatch')
@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class UserProfileView(TemplateView):
    template_name = 'accounts/profile.html'
