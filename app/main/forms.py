from django.forms import (
    ModelForm, TextInput, NumberInput, TimeInput
)

from .models import MessageETHContactID


class MessageETHContactIDForm(ModelForm):
    class Meta:
        model = MessageETHContactID
        fields = [
            "message",
            "user",
            "uid",
            "object",
            "type",
            "code",
            "section",
            "area",
            "time_stamp"
        ]
        widgets = {
            "message": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input message'
                }
            ),
            "user": NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input user'
                }
            ),
            "uid": NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input uid'
                }
            ),
            "object": NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input object'
                }
            ),
            "type": NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input type'
                }
            ),
            "code": NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input code'
                }
            ),
            "section": NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input section'
                }
            ),
            "area": NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input area'
                }
            ),
            "time_stamp": TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input timestamp'
                }
            ),
        }
