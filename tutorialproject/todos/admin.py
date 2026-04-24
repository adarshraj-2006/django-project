from django.contrib import admin

# Register your models here.
from .models import Todo,person
admin.site.register(Todo)
admin.site.register(person)