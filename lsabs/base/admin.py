from django.contrib import admin
from .models import Firm, Subsidiary, Project

# Register your models here.
admin.site.register(Firm)
admin.site.register(Subsidiary)
admin.site.register(Project)
