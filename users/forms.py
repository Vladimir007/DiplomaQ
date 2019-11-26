from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from users.models import User


class AuthForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder': _('Username'), 'autofocus': True}))
    password = forms.CharField(
        label=_("Password"), strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': _('Password')}),
    )


class RegisterForm(UserCreationForm):
    form_columns = (
        ('username', 'password1', 'password2'),
        ('email', 'first_name', 'last_name'),
    )
    first_name = forms.CharField(label=_('First name'), max_length=30, required=True)
    last_name = forms.CharField(label=_('Last name'), max_length=150, required=True)

    class Meta:
        model = User
        field_classes = {'username': UsernameField}
        fields = ('username', 'email', 'first_name', 'last_name')


class EditProfileForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("Passwords don't match."),
    }

    new_password1 = forms.CharField(label=_("New password"), widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label=_("New password confirmation"), required=False, widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        elif password2:
            # Validate if passwords similar and both specified
            password_validation.validate_password(password2, self.instance)
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["new_password1"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
