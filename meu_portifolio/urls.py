from django.contrib import admin
from django.urls import path, include
from minha_pessoa_app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('Eu/', include('minha_pessoa_app.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

