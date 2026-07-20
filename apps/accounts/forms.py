from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.accounts.models import UserProfile

class SignUpForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'mobile_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)

        UserProfile.objects.create(
            user = user,
            mobile_number = self.cleaned_data['mobile_number']
        )

        return user
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mobile_number',)