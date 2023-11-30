from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewset

router = DefaultRouter()
router.register(r'profiles', ProfileViewset)

urlpatterns = [
    path('', include(router.urls)),
    # ... other paths
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
