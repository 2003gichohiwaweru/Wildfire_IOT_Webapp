from django import forms

from main.models import Greenhouses


class GreenhouseForm(forms.ModelForm):
    class Meta:
        model = Greenhouses
        fields = ['flower_type', 'name', 'area', 'temperature', 'humidity', 'light_intensity', 'growing_style']