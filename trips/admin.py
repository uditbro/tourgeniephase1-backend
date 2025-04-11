from django.contrib import admin
from .models import Trip

class Tripmanager(admin.ModelAdmin):
    list_display=["user","source","destination","start_date","end_date","budget","created_at"]
    ordering=["created_at"]
    list_filter=["user","created_at","source","destination"]




admin.site.register(Trip, Tripmanager)