from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile




class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(
         attrs={
             'class': 'form-control',
             'placeholder': 'Enter your first name '
             }))
    last_name = forms.CharField(widget=forms.TextInput(
         attrs={
             'class': 'form-control',
             'placeholder': 'Enter your last name '
             }))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
        'placeholder':'Username max 150 characters. May contain alphanumeric, _, @, +, . and - characters.'
         }))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter email address',
            'required': 'False'
              }))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
             'placeholder': 'Enter Password'
             }))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={ 
         'class': 'form-control',
         'placeholder': 'Re enter Password'
        }
         ))
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
        'first_name',
        'last_name',
        'username',
        'email',
        'password1',
        'password2'
        ]


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
        'placeholder': 'Enter your first name '
        }
        ))
    last_name = forms.CharField(widget=forms.TextInput( 
        attrs={
        'class': 'form-control',
        'placeholder': 'Enter your last name '
    }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username max 150 characters. May contain alphanumeric, _, @, +, . and - characters.'
            }
            ))
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                 'placeholder': 'Enter email address', 
                 'required': 'False'
            }
            ))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email']


class ProfileUpdateForm(forms.ModelForm):
    birth_date = forms.CharField(widget=forms.widgets.DateInput(format="%Y-%m-%d",
        attrs={
            "type": "date",
            "class": "datepicker"
        }
        ))


    location = forms.CharField(widget=forms.TextInput(
         attrs={
             'placeholder': 'Enter your location'
             }
             ))

    about = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Tell us more about yourself'
         }))
    goals = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'What are your goals?',
             'required': 'False'
            }
            ))
    reason_join = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'What is your reason for joining? ',
            'required': 'False'
            }
           ))
    image = forms.ImageField(
      
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].queryset = Profile.objects


    class Meta:
        model = Profile
        fields = [
        'birth_date',
        'location',
        'about',
        'goals',
        'reason_join',
        'image']
