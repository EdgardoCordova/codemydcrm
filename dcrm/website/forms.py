# formulario creado por Django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Direccion Email'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    last_name =  forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))

    class Meta:
        model = User
        fields =  ('username', 'first_name', 'last_name', 'email', 'password1', 'password2') # no se pueden cambiar password1 y password2


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'entre Contrasenia'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme Contrasenia'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Nombre', 'class':'form-control'})) 
    last_name = forms.CharField(label='',required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Apellido', 'class':'form-control'}))
    email = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email', 'class':'form-control'}))
    phone = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Telefono', 'class':'form-control'}))
    address = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Direccion', 'class':'form-control'}))
    city = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Ciudad', 'class':'form-control'}))
    state = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Estado', 'class':'form-control'}))
    zipcode =forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Codigo ZIP', 'class':'form-control'}))

    class Meta:
        model = Record
        exclude = ('user',)     # inclulira todos los demás


