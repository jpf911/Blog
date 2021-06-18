from django.contrib import admin
from django.urls import path,include
# from .settings import DEBUG, STATIC_URL, STATICFILES_DIRS , MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myblog_app.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# if DEBUG:
    # urlpatterns += static(STATIC_URL,document_root =STATICFILES_DIRS )
    # urlpatterns += static(MEDIA_URL,document_root = MEDIA_ROOT)