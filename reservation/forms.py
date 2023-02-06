from django.forms import ModelForm, Select, TextInput, CheckboxInput, CheckboxSelectMultiple
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from reservation.models import *


class PreferenceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = PreferenceModel
        fields = '__all__'
        
        
class TableForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = TableModel
        fields = '__all__'


class ReservationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ReservationModel
        fields = '__all__'
        widgets = {
            'date': TextInput(attrs={
                'type': 'date',
            }),

            'time': TextInput(attrs={
                'type': 'time',
            })
        }

