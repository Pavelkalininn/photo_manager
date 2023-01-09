import os
from http import HTTPStatus

from api.filters import FaceFilter, PhotoFilter
from api.serializers import (FaceSerializer, PhotoListSerializer,
                             PhotoSerializer)
from django.http import FileResponse
from django_filters.rest_framework import DjangoFilterBackend
from photo.models import Face, Photo
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from manager.settings import MEDIA_ROOT


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAuthenticated, ]
    filterset_class = PhotoFilter
    filterset_fields = (
        'date',
        'gps_latitude',
        'gps_longitude',
        'names',
        'description'
    )

    def get_serializer_class(self):
        if not self.kwargs.get('pk') and self.request.method in ('GET',):
            return PhotoListSerializer
        return PhotoSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        filename = str(instance.image).split('/')[-1]
        os.remove(f'{MEDIA_ROOT}/{filename}')


class FaceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAuthenticated, ]
    filterset_class = FaceFilter
    filterset_fields = ('name', )


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def media(request, url):
    return FileResponse(
        open(f'{MEDIA_ROOT}/{url}', 'rb'),
        status=HTTPStatus.OK,
        as_attachment=True,
        filename=url
    )
