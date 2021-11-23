from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app import views
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('api', views.employee_data)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(router.urls))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
