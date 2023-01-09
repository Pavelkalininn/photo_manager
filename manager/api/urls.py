from api.views import FaceViewSet, PhotoViewSet, media
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

router.register('photos', PhotoViewSet, basename='photo-list')
router.register('faces', FaceViewSet, basename='face-list')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('media/<str:url>/', media)
]
