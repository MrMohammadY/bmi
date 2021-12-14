from django.contrib import admin
from django.urls import include, re_path
from django.urls import path
from django.views.generic import TemplateView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="BMI Calculator API",
        default_version='v1',
        description="BMI Calculator a calculator which calculate your body mass index(BMI)",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mehdy.work@gmail.com"),
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('bmi/', include('bmi_calculator.urls', namespace='bmi')),
    # ------------- swagger ------------- #
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # ------------- swagger ------------- #
]
