from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm

from .models import AdvUser


class RegisterForm(ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Passwords don\'t match.'
                                        )
    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data.get('password2'))
        if commit:
            user.save()
        return  user

    class Meta:
        model = AdvUser
        fields = ['login', "username", "password", "email", "pd_agree"]

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }