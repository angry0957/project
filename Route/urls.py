from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r'', views.RouteViewSet, base_name='Route')
urlpatterns = router.urls
