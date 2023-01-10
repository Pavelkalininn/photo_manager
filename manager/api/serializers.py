from drf_extra_fields.fields import (
    Base64ImageField,
)
from photo.models import (
    Face,
    Photo,
)
from rest_framework.fields import (
    CharField,
    DateField,
    FloatField,
)
from rest_framework.relations import (
    PrimaryKeyRelatedField,
    StringRelatedField,
)
from rest_framework.serializers import (
    ModelSerializer,
)


class FaceSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Face


class PhotoListSerializer(ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        fields = [
            'id',
            'image',
        ]
        model = Photo


class PhotoReadSerializer(PhotoListSerializer):
    date = DateField(required=False)
    gps_latitude = FloatField(required=False)
    gps_longitude = FloatField(required=False)
    names = StringRelatedField(many=True)
    description = CharField(required=False)

    class Meta:
        parent_fields = list(PhotoListSerializer.Meta.fields)
        parent_fields += [
            'date',
            'gps_latitude',
            'gps_longitude',
            'names',
            'description'
        ]
        fields = parent_fields
        model = Photo


class PhotoSerializer(PhotoListSerializer):
    names = PrimaryKeyRelatedField(
        queryset=Face.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        fields = list(PhotoReadSerializer.Meta.fields)
        model = Photo

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return PhotoReadSerializer(instance, context=context).data
