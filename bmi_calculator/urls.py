from django.urls import path

from bmi_calculator.views import BMIView

app_name = 'bmi'
urlpatterns = [
    path('calculator/', BMIView.as_view(), name='bmi-calculator'),
]
