from django import (
    forms,
)
from photo.models import (
    Photo,
)

from manager.settings import (
    PHOTO_FILTER_FIELDS,
)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = (
            *PHOTO_FILTER_FIELDS,
            'image'
        )
