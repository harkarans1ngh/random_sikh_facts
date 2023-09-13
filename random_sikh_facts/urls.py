"""
URL configuration for random_sikh_facts project.
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/facts/", include('facts.urls'))
]
