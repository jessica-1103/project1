from django.contrib import admin
from .models import Articulo, Autor
# Register your models here.
@admin.register(Autor, Articulo)
class AuthorAdmin(admin.ModelAdmin):
    pass


