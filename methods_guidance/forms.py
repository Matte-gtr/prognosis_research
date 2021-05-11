from django import forms
from .models import Textbook


class TextbookForm(forms.ModelForm):
    class Meta:
        model = Textbook
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'optional_link': forms.TextInput(attrs={'class': 'form-control'}),
            'optional_link_text': forms.TextInput(
                attrs={'class': 'form-control'}),
        }
    image = forms.ImageField(required=False)
