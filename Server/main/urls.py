from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home),  
    path('Index.html', views.home),
    path('add_device.html', views.addDevice),
    path('remove_device.html', views.removeDevice),
    path('home.html', views.main),
    path('add_image.html',views.addNewImage),
    path('unlock_door.html', views.unlockDoor)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
