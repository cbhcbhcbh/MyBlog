import logging

from django.contrib import admin
from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings

logger = logging.getLogger('tuna')
logger.debug('This is debug message')
logger.info('This is info message')


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'mdeditor', include('mdeditor.urls')),
    re_path(r'', include(('blog.urls', 'blog'), namespace='blog')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
