from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet, ComedyViewSet

# Create a router and register our viewset with it.
router = routers.SimpleRouter()
router.register('movies', MovieViewSet)
router.register('action', ActionViewSet, basename='action')
router.register('comedy', ComedyViewSet, basename='comedy')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('admin/', admin.site.urls),
]
