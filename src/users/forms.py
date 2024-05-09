from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ExtendedUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2')
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Perform validation for Kenyan phone number format
        # Example: Check if it starts with '+254' or '0' and has 9 digits
        # Add your validation logic here
        return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                first_name=self.cleaned_data.get('first_name'),
                last_name=self.cleaned_data.get('last_name'),
                phone_number=self.cleaned_data.get('phone_number'),
                email_address=self.cleaned_data.get('email'),
            )
        return user