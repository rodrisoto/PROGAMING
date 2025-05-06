from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Usuario, Juegos, Categoria 
from datetime import date
import re



class RegistroUsuarioForm(UserCreationForm):
    # Campos adicionales personalizados
    nombre_completo = forms.CharField(max_length=255, required=True, label="Nombre Completo")
    correo = forms.EmailField(required=True, label="Correo Electrónico")
    fecha_nacimiento = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2025)), label="Fecha de Nacimiento")
    plataforma = forms.ChoiceField(
        choices=[('pc', 'PC'), ('playstation', 'PlayStation'), ('xbox', 'Xbox'),
                 ('nintendo', 'Nintendo'), ('movil', 'Móvil')],
        required=False, label="Plataforma Favorita"
    )
    direccion = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Ingresa tu dirección completa'}), 
        required=False, label="Dirección de Despacho"
    )
    terminos = forms.BooleanField(required=True, label="Acepto los términos y condiciones")

    # Meta configurada para trabajar con el modelo Usuario
    class Meta:
        model = Usuario
        fields = ('username', 'nombre_completo', 'correo', 'password1', 'password2', 'fecha_nacimiento', 'plataforma', 'direccion', 'terminos')

    # Validación personalizada para el correo electrónico
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if Usuario.objects.filter(email=correo).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return correo

    # Validación personalizada para la fecha de nacimiento (al menos 18 años)
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento > date.today().replace(year=date.today().year - 18):
            raise ValidationError("Debes ser mayor de 18 años para registrarte.")
        return fecha_nacimiento

    # Validaciones para contraseñas
    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        # Longitud mínima de 8 caracteres
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        
        # Uso de al menos un carácter especial
        if not re.search(r'[@#$%^&+=]', password):
            raise ValidationError("La contraseña debe contener al menos un carácter especial como @, #, $, %, ^, &, +, =.")
        
        # Uso de al menos un número
        if not re.search(r'\d', password):
            raise ValidationError("La contraseña debe contener al menos un número.")
        
        # Uso de al menos una letra mayúscula
        if not re.search(r'[A-Z]', password):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")

        return password

    # Validación para el nombre de usuario (mínimo 4 caracteres)
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise ValidationError("El nombre de usuario debe tener al menos 4 caracteres.")
        return username

    # Método para guardar el usuario con los campos adicionales
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['nombre_completo']
        user.email = self.cleaned_data['correo']
        user.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        user.direccion = self.cleaned_data.get('direccion')
        user.plataforma = self.cleaned_data.get('plataforma')
        
        # Puedes agregar otras personalizaciones aquí
        if commit:
            user.save()
        return user


class JuegosForm(forms.ModelForm):
    class Meta:
        model = Juegos
        fields = ['nombre', 'precio', 'descripcion', 'categoria', 'stock', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

