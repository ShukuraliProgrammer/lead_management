from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



schema_view = get_schema_view(
   openapi.Info(
      title="Lead Management API",
      default_version='v1',
      description="This is TESTING project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shukurdev2002@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('applications/', include('application.urls')),
    # API Documentation url
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)