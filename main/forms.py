from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["name", "email", "phone", "service", "description", "image"]
        widgets = {
            "service": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }
