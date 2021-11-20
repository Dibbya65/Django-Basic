from django.contrib import admin

# Register your models here.
from .models import Portfolio, Team

admin.site.register(Team)
admin.site.register(Portfolio)
