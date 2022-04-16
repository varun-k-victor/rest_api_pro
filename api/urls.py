from django.urls import path,include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register('Info',views.InfoViewSet)

urlpatterns = [
    path('',include(router.urls))
]
