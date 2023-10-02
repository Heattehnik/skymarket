from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ads.apps import SalesConfig
from ads.views import AdViewSet, UserAdsListView, AdCommentsView, CreateCommentView

ad = DefaultRouter()
ad.register(r"ads", AdViewSet, basename="ads")
# TODO настройка роутов для модели
app_name = SalesConfig.name

urlpatterns = [
    path('ads/me/', UserAdsListView.as_view(), name='me_ads'),
    path('ads/<int:ad_id>/comments/', AdCommentsView.as_view(), name='ad_comments'),
    path('ads/<int:ad_pk>/comments/', CreateCommentView.as_view(), name='create_comment'),
] + ad.urls
