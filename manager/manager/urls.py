from django.conf.urls import (
    url,
)
from django.contrib import (
    admin,
)
from django.urls import (
    include,
    path,
)
from drf_yasg import (
    openapi,
)
from drf_yasg.views import (
    get_schema_view,
)
from rest_framework import (
    permissions,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Photo manager API",
        default_version='v1',
        description="Документация для приложения photo manager",
        contact=openapi.Contact(email="kalinin@sert.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('web.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_errror'
handler403 = 'core.views.csrf_failure'
