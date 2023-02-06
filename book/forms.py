from django.forms import ModelForm, Select, TextInput, CheckboxInput, CheckboxSelectMultiple
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from book.models import *


class BookCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = BookCategoryModel
        fields = '__all__'


class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = BookModel
        fields = '__all__'

