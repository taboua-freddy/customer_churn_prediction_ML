from django.contrib import admin
from django.urls import path,include
from ChurnAPI import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('ChurnAPI.urls'))
]
