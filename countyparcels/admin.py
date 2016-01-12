from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Counties #, State

#admin.site.register(State)
admin.site.register(Counties)