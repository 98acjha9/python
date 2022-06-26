from pydoc import plain
from django.contrib import admin
from .models import Plan
# Register your models here.


@admin.register(plain)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'item']
