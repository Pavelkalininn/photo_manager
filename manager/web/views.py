from http import (
    HTTPStatus,
)

from django.contrib.auth.decorators import (
    login_required,
)
from django.contrib.auth.forms import (
    UserCreationForm,
)
from django.http import (
    FileResponse,
)
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.urls import (
    reverse_lazy,
)
from django.views.generic import (
    CreateView,
)
from photo.models import (
    Photo,
)
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from web.forms import (
    PhotoForm,
)
from web.utils import (
    pagination,
)

from manager.settings import (
    MEDIA_ROOT,
    PHOTO_FILTER_FIELDS,
)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('web:login')
    template_name = 'registration/signup.html'


@login_required()
def index(request):
    photos = Photo.objects.prefetch_related('names').all()
    for key in PHOTO_FILTER_FIELDS:
        filter_parameter = request.GET.get(key)
        if filter_parameter:
            photos = photos.filter(**{key: filter_parameter})

    page_obj = pagination(photos, request)
    context = {
        'page_obj': page_obj,
        'title_text': 'Список фото'
    }
    return render(request, 'photos/index.html', context)


@login_required()
def photo_get(request, photo_id):
    photo = get_object_or_404(
        Photo.objects.prefetch_related('names').all(), pk=photo_id)
    # page_obj = pagination((equipment,), request)
    context = {
        'page_obj': (photo,),
        'title_text': 'Фотография'
    }
    return render(request, 'photos/index.html', context)


@login_required()
def photo_create(request):
    form = PhotoForm(request.POST or None, files=request.FILES or None, )
    if form.is_valid():
        photo = form.save()
        return redirect('web:photo_get', photo.pk)
    return render(
        request,
        'photos/create_form.html',
        {'form': form}
    )


@login_required()
def photo_edit(request, photo_id):
    photo = get_object_or_404(
        Photo.objects.prefetch_related('names').all(), pk=photo_id)
    form = PhotoForm(
        request.POST or None,
        files=request.FILES or None,
        instance=photo
    )
    if form.is_valid():
        photo = form.save()
        return redirect('web:photo_get', photo.pk)
    return render(
        request,
        'photos/create_form.html',
        {'form': form, 'is_edit': True}
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def media(request, url):
    return FileResponse(
        open(f'{MEDIA_ROOT}/{url}', 'rb'),
        status=HTTPStatus.OK,
        as_attachment=True,
        filename=url
    )
