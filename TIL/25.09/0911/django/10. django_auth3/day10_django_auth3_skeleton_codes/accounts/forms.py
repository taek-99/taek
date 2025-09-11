
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        


class CustomChangeUser(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name')