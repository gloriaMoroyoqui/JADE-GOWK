from django import forms
from django.contrib.auth.models import User
from .models import Perfil

# Formulario para registrar un nuevo usuario estilo Shein
class RegistroForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nombre Completo", 
        max_length=150, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'})
    )
    email = forms.EmailField(
        label="Correo Electrónico", 
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'})
    )
    username = forms.CharField(
        label="Nombre de Usuario (Login)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usuario123'})
    )
    password = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Crea una contraseña segura'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"]) # Encripta la contraseña de forma segura
        if commit:
            user.save()
        return user


# Formulario para actualizar Datos Básicos (Nombre y Correo)
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre Completo", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo Electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'email']


# Formulario para actualizar Datos Avanzados (Foto, Teléfono, Dirección)
class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto', 'telefono', 'direccion']
        widgets = {
            'foto': forms.FileInput(attrs={'class': 'form-control-file'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu teléfono'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tu dirección de envío'}),
        }