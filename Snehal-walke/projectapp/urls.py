
from django.contrib import admin
from django.urls import path, include
from loginlogout.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('loginlogout.urls')),
    path('', index, name="index"),
]
