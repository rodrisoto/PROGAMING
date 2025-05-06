from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Categoria, Juegos

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_admin', 'is_active', 'date_joined']
    list_filter = ['is_admin', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['date_joined']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'direccion')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'direccion')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )

# Registra el modelo Usuario con la clase personalizada en el admin
admin.site.register(Usuario, UsuarioAdmin)

# Registrar Categoria en el admin
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Categoria, CategoriaAdmin)


class JuegosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'stock', 'imagen')
    list_editable = ('precio', 'stock')
    search_fields = ('nombre', 'categoria__nombre')  
    list_filter = ('categoria',)  
    ordering = ('nombre',) 

admin.site.register(Juegos, JuegosAdmin)
