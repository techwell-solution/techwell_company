from django import forms

from .models import ContactMessage, Service


class ContactMessageForm(forms.ModelForm):

    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(is_active=True).order_by("order"),
        empty_label="Select a service",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = ContactMessage

        fields = [
            "name",
            "email",
            "phone",
            "subject",
            "service",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your Name",
                    "class": "form-control",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Your Email",
                    "class": "form-control",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Phone Number",
                    "class": "form-control",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "placeholder": "Subject",
                    "class": "form-control",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder": "Tell us about your project or inquiry...",
                    "class": "form-control",
                    "rows": 6,
                }
            ),
        }