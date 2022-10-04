from django import forms
from django.core.exceptions import ValidationError

PHONES = ['+375(29)',
          '+375(33)',
          '+375(25)',
          '+375(44)']

def login_validator(value):
    if value and value.isalpha():
        pass
    else:
        raise ValidationError(message='loginError')

def phone_validator(value):
    if value[:8] in PHONES and len(value) == 15:
        res = False
    else:
        res = True
    if res:
        raise ValidationError(message = 'phoneError')

def email_validator(value):
    if not ("@" in value):
        raise ValidationError(message='emailError')



class FormToValidate(forms.Form):
    login = forms.CharField(max_length=30,required=False,validators=[login_validator])
    phone = forms.CharField(max_length=30,required=False,validators=[phone_validator])
    email = forms.CharField(max_length=30,required=False,validators=[email_validator])