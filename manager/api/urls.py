from api.views import (
    FaceViewSet,
    PhotoViewSet,
)
from django.urls import (
    include,
    path,
)
from rest_framework import (
    routers,
)

router = routers.DefaultRouter()

router.register('photos', PhotoViewSet, basename='photo-list')
router.register('faces', FaceViewSet, basename='face-list')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
