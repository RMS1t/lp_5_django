from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import AdvUser


class RegisterForm(forms.ModelForm):

    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = AdvUser
        fields = ['login',"username", "password", "email",  "pd_agree"]
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != self.password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return AdvUser.set_password(self,raw_password=cd['password'])