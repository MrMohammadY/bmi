from django.contrib.gis.measure import Distance
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class BMICalculatorSerializer(serializers.Serializer):
    weight = serializers.FloatField(write_only=True, min_value=1)
    height = serializers.IntegerField(write_only=True)
    bmi = serializers.FloatField(read_only=True)
    message = serializers.CharField(read_only=True)

    @staticmethod
    def calculate_bmi(weight, height):
        return weight / height ** 2

    @staticmethod
    def create_bmi_message(bmi):
        msg = None
        if bmi <= 18.5:
            msg = f'Your status is: Light weight'
        elif 18.5 < bmi <= 24.9:
            msg = f'Your status is: Normal weight'
        elif 24.9 < bmi <= 29.9:
            msg = f'Your status is: Over weight'
        elif 29.9 < bmi <= 34.9:
            msg = f'Your status is: Fat'
        elif 34.9 < bmi <= 39.9:
            msg = f'Your status is: Obesity - Type 1'
        elif bmi > 39.9:
            msg = f'Your status is: Obesity - Type 2'
        return msg

    def validate(self, attrs):
        if isinstance(attrs.get('height'), int):
            height = Distance(cm=attrs.get('height'))
            attrs['height'] = height.m
            attrs['bmi'] = self.calculate_bmi(attrs.get('weight'), attrs.get('height'))
            attrs['message'] = self.create_bmi_message(attrs['bmi'])
            return attrs
        raise ValidationError('height most be integer!!')
