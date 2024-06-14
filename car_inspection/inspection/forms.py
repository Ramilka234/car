from django import forms
from .models import Inspection, Car, RegistrationRequest, Article
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
class EditInspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['date', 'passed', 'inspector_comments']
        widgets = {
            'date': forms.DateInput(),
            'passed': forms.CheckboxInput(),
            'inspector_comments': forms.Textarea(attrs={'rows': 4}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'vin', 'color', 'mileage', 'registration_number']


class RegistrationRequestForm(forms.ModelForm):
    class Meta:
        model = RegistrationRequest
        fields = ['car', 'request_type', 'request_date']
        widgets = {
            'request_date': forms.DateInput(attrs={'type': 'date'}),
            }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(user=user)

class EditRegForm(forms.ModelForm):
    class Meta:
        model = RegistrationRequest
        fields = ['car', 'request_type', 'request_date', 'approved']
        widgets = {
            'request_date': forms.DateInput(),
            'approved': forms.CheckboxInput(),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']