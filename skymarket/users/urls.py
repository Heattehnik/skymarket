from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from users.apps import UsersConfig
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

app_name = UsersConfig.name

users_router = SimpleRouter()

users_router.register("", UserViewSet, basename="users")

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(users_router.urls)),
]
