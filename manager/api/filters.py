from django_filters import CharFilter, FilterSet
from photo.models import Face, Photo


class PhotoFilter(FilterSet):
    date = CharFilter(
        lookup_expr='exact',
        field_name='date'
    )
    gps_latitude = CharFilter(
        lookup_expr='exact',
        field_name='gps_latitude'
    )
    gps_longitude = CharFilter(
        lookup_expr='exact',
        field_name='gps_longitude'
    )
    names = CharFilter(
        method='names_filter',
        field_name='names'
    )
    description = CharFilter(
        lookup_expr='icontains',
        field_name='description'
    )

    class Meta:
        model = Photo
        fields = (
            'date',
            'gps_latitude',
            'gps_longitude',
            'names',
            'description'
        )

    @staticmethod
    def names_filter(queryset, name, value):
        return queryset.filter(names__name__istartswith=value).distinct()


class FaceFilter(FilterSet):
    name = CharFilter(
        lookup_expr='istartswith',
        field_name='name'
    )

    class Meta:
        model = Face
        fields = ('name', )
