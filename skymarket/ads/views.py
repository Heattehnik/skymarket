from rest_framework import pagination, viewsets
from ads.paginators import AdsPaginator, CommentsPaginator
from ads.serializers import CommentSerializer, AdSerializer, AdDetailSerializer


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    pagination_class = AdsPaginator
    serializer_class = AdSerializer


class CommentViewSet(viewsets.ModelViewSet):
    pagination_class = CommentsPaginator
    serializer_class = CommentSerializer
