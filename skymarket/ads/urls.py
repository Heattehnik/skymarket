from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ads.apps import SalesConfig
from ads.views import AdViewSet

ad = DefaultRouter()
ad.register(r"habits", AdViewSet, basename="habits")
# TODO настройка роутов для модели
app_name = SalesConfig.name

urlpatterns = [

] + ad.urls
