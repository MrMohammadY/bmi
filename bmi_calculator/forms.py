from django import forms
from django.core.exceptions import ValidationError
from django.contrib.gis.measure import Distance


class BMIForm(forms.Form):
    weight = forms.FloatField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Input your weight as kg'})
    )
    height = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Input your height as cm'})
    )

    def clean_height(self):
        if isinstance(self.cleaned_data['height'], int):
            height = Distance(cm=self.cleaned_data['height'])
            self.cleaned_data['height'] = height.m
            return self.cleaned_data['height']
        raise ValidationError('height most be integer!!')
