from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Customising Admin Text
admin.site.site_header = 'Welcome To Admin Dashboard'
admin.site.index_title = 'Contacts'
admin.site.site_title = 'Dashboard'


