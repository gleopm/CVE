from django.contrib import admin
from django.urls import path, include
from CVEapi.views import home  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CVE/', include('CVEapi.urls')),
    path('', home, name='home'),  
]