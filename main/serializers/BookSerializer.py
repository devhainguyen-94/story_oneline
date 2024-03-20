from rest_framework import serializers ,permissions
from main.models import Book , CustomUser , Category
from main.serializers.UserSerializer import UserSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','description','category', 'auth']
        # read_only_fields = ('created_by',)
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    auth = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    extra_kwargs = {'auth_id': {'default': serializers.CurrentUserDefault()}}
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        return category_data
        # category, _ = Category.objects.get_or_create(**category_data)
        # instance = Book.objects.create(category=category, **validated_data)
        # return instance
        # return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        # instance.name = validated_data.get('description', instance.description)
        instance.save()
        return instance