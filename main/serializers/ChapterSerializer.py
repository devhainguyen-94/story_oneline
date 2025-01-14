from rest_framework import serializers ,permissions
from main.models import Chapter , CustomUser , Book
from main.serializers.UserSerializer import UserSerializer
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id','title', 'created_by', 'book','image','content','description']
    id = serializers.IntegerField(read_only=True)
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    content = serializers.CharField(required= True)
    description = serializers.CharField(required=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    image = serializers.ImageField(required=False)
    title = serializers.CharField(required=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        book_data = validated_data.pop('book')  # Lấy danh sách các category từ dữ liệu đã được xác nhận
        chapter = Chapter.objects.create(book= book_data,**validated_data)  # Tạo một đối tượng Book mới

        # Gán các category cho đối tượng Book sử dụng phương thức set()
        # book.category.set(categories_data)
        return chapter
        # return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Chapter` instance, given the validated data.
        """
        if 'image' in validated_data:
            instance.image = validated_data.get('image', instance.image)
        instance.title = validated_data.get('title', instance.title)
        # instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance