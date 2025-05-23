from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'age')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = UserChangeForm.Meta.fields + 'age', 'email'