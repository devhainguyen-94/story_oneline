from rest_framework import serializers ,permissions
from main.models import Category , CustomUser
from main.serializers.UserSerializer import UserSerializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'created_by']
        # read_only_fields = ('created_by',)
    id = serializers.IntegerField(read_only=True)
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    name = serializers.CharField(required=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance