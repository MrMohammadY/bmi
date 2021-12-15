from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bmi_calculator.api.serializers import BMICalculatorSerializer


class BMICalculatorAPIView(GenericAPIView):
    """
        post:
        Calculate BMI with your weight and height and return result as bmi and description about your body
    """
    serializer_class = BMICalculatorSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
