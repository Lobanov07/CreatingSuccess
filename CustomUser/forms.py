from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

user = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = user
        fields = ("username", "email", "password1", "password2")


class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ["username", "bio", "date_of_birth",
                  "profile_picture", "phone_number",
                  "first_name", 'last_name']
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }
