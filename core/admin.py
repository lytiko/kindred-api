from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.register(Tier)
admin.site.register(Category)
admin.site.register(Person)