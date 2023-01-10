from django.urls import (
    include,
    path,
)
from web import (
    views,
)
from web.views import (
    SignUpView,
    media,
)

app_name = "web"

urlpatterns = [
    path('', views.index, name="index"),
    path('', include('django.contrib.auth.urls')),
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        'photo_get/<int:photo_id>/',
        views.photo_get,
        name='photo_get'
    ),
    path(
        'photo_create/',
        views.photo_create,
        name='photo_create'
    ),
    path(
        'photo_edit/<int:photo_id>/',
        views.photo_edit,
        name='photo_edit'
    ),
    path('media/<str:url>/', media),
]
