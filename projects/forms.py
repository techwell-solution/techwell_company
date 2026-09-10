from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            "name",
            "email",
            "phone",
            "service",
            "description",
            "website_url",
            "budget",
            "preferred_date",
            "priority",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your full name",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "you@example.com",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "+254 7XX XXX XXX",
            }),

            "service": forms.Select(attrs={
                "class": "form-control",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": (
                    "Tell us about your project, requirements, "
                    "features, or goals..."
                ),
                "rows": 6,
            }),

            "website_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://example.com",
            }),

            "budget": forms.Select(attrs={
                "class": "form-control",
            }),

            "preferred_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),

            "priority": forms.Select(attrs={
                "class": "form-control",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Only show active TechWell Company services
        self.fields["service"].queryset = (
            self.fields["service"]
            .queryset
            .filter(is_active=True)
            .order_by("order", "title")
        )