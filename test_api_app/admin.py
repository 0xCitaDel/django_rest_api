from django.contrib import admin
from .models import TestModel, ModelX

admin.site.register((TestModel, ModelX))