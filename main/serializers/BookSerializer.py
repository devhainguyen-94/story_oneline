from rest_framework import serializers ,permissions
from main.models import Category , CustomUser , Book
from main.serializers.UserSerializer import UserSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'auth', 'category','image']
        # read_only_fields = ('created_by',)
    id = serializers.IntegerField(read_only=True)
    auth = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    title = serializers.CharField(required=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    extra_kwargs = {'auth': {'default': serializers.CurrentUserDefault()}}
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        categories_data = validated_data.pop('category')  # Lấy danh sách các category từ dữ liệu đã được xác nhận
        book = Book.objects.create(**validated_data)  # Tạo một đối tượng Book mới

        # Gán các category cho đối tượng Book sử dụng phương thức set()
        book.category.set(categories_data)

        return book
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance