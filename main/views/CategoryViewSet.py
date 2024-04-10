from rest_framework import generics
from main.models import Category
from main.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins , viewsets,status
from rest_framework.decorators import api_view, permission_classes
from main.permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response
class CategoryListCreateAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request)
        # Kiểm tra xem người dùng hiện tại có phải là người tạo ra category hay không
        if instance.created_by != request.user:
            return Response({"error": "You do not have permission to delete this category"},
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsOwner]


class CategoryDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=404)

        # Kiểm tra xem người dùng có quyền xóa category hay không
        if category.created_by != request.user:
            return Response({"error": "You do not have permission to delete this category11111"}, status=403)
        category.delete()
        return Response({"success": "Category deleted successfully"}, status=204)