from django.contrib import admin
from .models import CustomUser

class Customusermanage(admin.ModelAdmin):
    list_display=["id","email","username"]
    ordering=["id"]

admin.site.register(CustomUser,Customusermanage)