from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from ads.models import Ad, Comment
from ads.paginators import AdsPaginator, CommentsPaginator
from ads.serializers import CommentSerializer, AdSerializer, AdDetailSerializer


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    pagination_class = AdsPaginator
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

    def perform_create(self, serializer):
        # Получите текущего пользователя (автора объявления)
        author = self.request.user

        # Сохраните объект объявления с указанным автором
        serializer.save(author=author)

        # Форматируйте JSON-ответ, включая данные об авторе
        data = {
            "pk": serializer.instance.pk,
            "image": serializer.instance.image.url if serializer.instance.image else "",
            "title": serializer.validated_data["title"],
            "price": serializer.validated_data["price"],
            "phone": serializer.validated_data["phone"],
            "description": serializer.validated_data["description"],
            "author_first_name": author.first_name,
            "author_last_name": author.last_name,
            "author_id": author.id,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserAdsListView(ListAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        # Получите текущего пользователя
        user = self.request.user

        # Получите все объявления, созданные текущим пользователем
        queryset = Ad.objects.filter(author=user)

        return queryset


class AdCommentsView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'ad_id'  # Set the lookup field to 'ad_id'

    def get_queryset(self):
        # The 'ad_id' parameter is now used as the lookup field
        ad_id = self.kwargs.get('ad_id')
        queryset = Comment.objects.filter(ad_id=ad_id)
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    pagination_class = CommentsPaginator
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CreateCommentView(CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        # Получите текущего пользователя (автора объявления)
        author = self.request.user

        # Сохраните объект объявления с указанным автором
        serializer.save(author=author)


