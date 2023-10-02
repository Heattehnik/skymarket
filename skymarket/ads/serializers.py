from rest_framework import serializers

from ads.models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_id = serializers.ReadOnlyField(source='author.id')
    phone = serializers.ReadOnlyField(source='author.phone')

    class Meta:
        model = Ad
        fields = (
            'pk', 'image', 'title', 'price', 'phone',
            'description', 'author_first_name', 'author_last_name', 'author_id',
        )


class AdDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = "__all__"
