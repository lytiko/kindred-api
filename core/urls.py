from django.urls import path
from django.contrib import admin
from core.views import *

urlpatterns = [
 path("admin/", admin.site.urls),
 path("", home, name="home")
]