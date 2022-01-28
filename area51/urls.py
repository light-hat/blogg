from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls'))
]

handler400 = "area51.views.bad_request_view"
handler403 = "area51.views.access_denied_view"
handler404 = "area51.views.page_not_found_view"
handler405 = "area51.views.not_allowed_view"
handler408 = "area51.views.timeout_view"
handler500 = "area51.views.server_error_view"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)