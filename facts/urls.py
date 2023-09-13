# urls.py

from django.urls import path, include
from rest_framework import routers

from facts.views import FactViewSet

router = routers.DefaultRouter()
router.register('', FactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]