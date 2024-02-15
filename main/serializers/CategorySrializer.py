from rest_framework import serializers
from .main.models import Category


class CategorySrializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'created_by', ]
    id = serializers.IntegerField(read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.title)
        # instance.code = validated_data.get('code', instance.code)
        # instance.linenos = validated_data.get('linenos', instance.linenos)
        # instance.language = validated_data.get('language', instance.language)
        # instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance