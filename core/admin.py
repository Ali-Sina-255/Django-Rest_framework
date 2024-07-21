from django.contrib import admin

# Register your models here.
from .models import Superviser, Memebership, Project


admin.site.register(Superviser)
admin.site.register(Memebership)
admin.site.register(Project)
