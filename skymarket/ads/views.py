from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ads.models import Ad, Comment
from ads.paginators import AdsPaginator, CommentsPaginator
from ads.serializers import CommentSerializer, AdSerializer, AdDetailSerializer
from rest_framework.permissions import IsAuthenticated


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
            "title": serializer.data["title"],
            "price": serializer.data["price"],
            "phone": serializer.data["phone"],
            "description": serializer.data["description"],
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


class AdCommentRetrieve(ViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=['get'], detail=True)
    def retrieve(self, request, ad_id, comment_id):
        try:
            # Получите комментарий по заданному comment_id
            comment = Comment.objects.get(pk=comment_id)

            # Создайте сериализатор для комментария
            serializer = CommentSerializer(comment)

            return Response(serializer.data)

        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['patch'], detail=True)
    def change(self, request, ad_id, comment_id):
        try:
            # Получите комментарий по заданному comment_id
            comment = Comment.objects.get(pk=comment_id)

            # Примените данные из PATCH-запроса к комментарию
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['delete'], detail=True)
    def destroy(self, request, ad_id, comment_id):
        try:
            # Получите комментарий по заданному comment_id
            comment = Comment.objects.get(pk=comment_id)

            # Удалите комментарий
            comment.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AdCommentsView(ViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=['get'], detail=True)
    def list(self, request, ad_id=None):
        # Обработка GET-запросов

        # Извлечение ad_id из URL и использование его для получения комментариев
        ad_id = self.kwargs.get('ad_id')
        queryset = Comment.objects.filter(ad_id=ad_id)

        # Вы можете добавить дополнительную логику здесь, если это необходимо

        # Создание сериализатора для комментариев и сериализация данных
        serializer = CommentSerializer(queryset, many=True)

        # Возврат сериализованных данных в HTTP-ответе
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def create(self, request, ad_id=None):
        # Получите текущего пользователя (автора комментария)
        author = request.user

        # Извлечь данные из запроса
        comment_data = request.data

        # Создать новый комментарий с ad_id из URL, данными из запроса и автором
        new_comment = Comment.objects.create(ad_id=ad_id, author=author, **comment_data)

        # Вернуть HTTP-ответ с информацией о созданном комментарии
        serializer = CommentSerializer(new_comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = CommentsPaginator
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
