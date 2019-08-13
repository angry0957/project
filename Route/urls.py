from django.urls import path

from . import views
from jsonModel import views as myview
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register('route', views.RouteViewSet, base_name='Route')
router.register('data', views.DataViewSet, base_name='Data')
router.register('json', myview.JsonModelViewSet, base_name='Json')
urlpatterns = router.urls
