from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet, ComedyViewSet
from django.conf.urls.static import static
from django.conf import settings

# Create a router and register our viewset with it.
router = routers.SimpleRouter()
router.register('movies', MovieViewSet)
router.register('action', ActionViewSet, basename='action')
router.register('comedy', ComedyViewSet, basename='comedy')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
