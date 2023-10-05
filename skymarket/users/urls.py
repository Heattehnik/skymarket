from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from users.apps import UsersConfig
from users.views import UserView

app_name = UsersConfig.name

users_router = SimpleRouter()

users_router.register("", UserViewSet, basename="users")

urlpatterns = [
    path('users/me/', UserView.as_view(), name="user_retrieve"),
    path("", include(users_router.urls)),
]
