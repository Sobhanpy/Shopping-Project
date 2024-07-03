from django import forms
from accounts.models import Profile

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["user", "first_name", "last_name", "image", "phone", "address"]