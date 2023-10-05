from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source='author.id')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    ad_id = serializers.ReadOnlyField(source='ad.id')
    # TODO avatars/default.png 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
    # author_image = serializers.ReadOnlyField(source='author.avatar')

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author_id', 'author_first_name', 'author_last_name', 'created_at', 'ad_id')


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
