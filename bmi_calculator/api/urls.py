from django.urls import path
from bmi_calculator.api.views import BMICalculatorAPIView

app_name = 'api'

urlpatterns = [
    path('calculator/', BMICalculatorAPIView.as_view(), name='bmi-calculator'),
]
