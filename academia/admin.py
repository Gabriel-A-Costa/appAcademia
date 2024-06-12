from django.contrib import admin
from .models import Aparelho, Exercicio, Room

# Register your models here.
admin.site.register(Aparelho)
admin.site.register(Exercicio)
admin.site.register(Room)