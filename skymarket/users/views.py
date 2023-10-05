from djoser.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from users.models import User
from users.serializers import CurrentUserSerializer


class UserView(APIView):
    serializer_class = CurrentUserSerializer
    queryset = User.objects.all()
