from django import forms
from . import models


class ApplicantForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=models.CHRFIELD_LEN,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your first name',
        }),
    )

    last_name = forms.CharField(
        max_length=models.CHRFIELD_LEN,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your last name',
        }),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email address',
        }),
    )

    phone = forms.CharField(
        max_length=models.CHRFIELD_LEN,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your phone number',
        }),
    )

    date_available = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
        }),
    )

    resume = forms.FileField()

    class Meta:
        model = models.Applicant
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'date_available',
            'resume',
        )
