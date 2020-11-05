from django.forms import (
    ModelForm, TextInput, NumberInput
)

from .models import AdemcoCode


class AdemcoCodeForm(ModelForm):
    class Meta:
        model = AdemcoCode
        fields = ["contact_code", "text_code", "message_type"]
        widgets = {
            "contact_code": NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input contact code'
                }
            ),
            "text_code": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input text code'
                }
            ),
            "message_type": NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input message type'
                }
            )
        }
