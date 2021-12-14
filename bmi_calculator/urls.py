from django.urls import path, include

from bmi_calculator.views import BMIView

app_name = 'bmi'
urlpatterns = [
    path('calculator/', BMIView.as_view(), name='bmi-calculator'),
    path('api/', include('bmi_calculator.api.urls', namespace='api')),
]
