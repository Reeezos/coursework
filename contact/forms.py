from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """Subscribe to email form"""
    class Meta:
        model = Contact
        fields = ("email", )
        widgets = {
            "email": forms.EmailInput(attrs={"class": "editContent", "placeholder": "Введіть вашу пошту...",})
        }
        labels = {
            "email": ''
        }
