from rest_framework import serializers ,permissions
from main.models import Category , CustomUser , Book
from main.serializers.UserSerializer import UserSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'auth', 'category','image']
    id = serializers.IntegerField(read_only=True)
    auth = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    image = serializers.ImageField(required=False)
    title = serializers.CharField(required=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    extra_kwargs = {'auth': {'default': serializers.CurrentUserDefault()}}
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        categories_data = validated_data.pop('category', [])

        # Tạo một đối tượng Book từ dữ liệu đã được validate
        book = Book.objects.create(**validated_data)

        # Liên kết các category với đối tượng Book mới được tạo
        for category in categories_data:
            book.category.add(category)
        return book
        # return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        if 'image' in validated_data:
            instance.image = validated_data.get('image', instance.image)
        instance.title = validated_data.get('title', instance.title)
        # instance.author = validated_data.get('author', instance.author)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance