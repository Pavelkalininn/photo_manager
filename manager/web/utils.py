from django.core.paginator import (
    Paginator,
)

from manager.settings import (
    COUNT_PHOTO_ON_PAGE,
)


def pagination(photos, request):
    paginator = Paginator(photos, COUNT_PHOTO_ON_PAGE)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
