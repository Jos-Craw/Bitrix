from django.forms import ModelForm
from django import forms
from .models import Application, AdvUser, PriceList
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


# class ApplicationForm(ModelForm):
#     class Meta:
#         model = Application
#         fields = '__all__'


class AddPriceToApplicationForm(ModelForm):
    class Meta:
        model = PriceList
        fields = '__all__' 



class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,)
    password2 = forms.CharField(label='Password(repeat)', widget=forms.PasswordInput)

    def clean_passwird1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Passwords do not match',
                                                   code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username','department', 'password1', 'password2',
                  'first_name', 'last_name')
