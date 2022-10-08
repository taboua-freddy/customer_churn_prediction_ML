from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ChurnAPI', views.ChurnsView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('status/', views.churnreject),
    path('forms/', views.cxcontact,name='cxform'),
]