from rest_framework import generics
from main.models import Book ,Category
from main.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins , viewsets

class BookListCreateAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(auth = self.request.user)

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            category = Category.objects.get(id=category_id)
            return category.book_set.all()
            # return Book.objects.filter(category_id=category_id)
        return Book.objects.all()
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request)
        # Kiểm tra xem người dùng hiện tại có phải là người tạo ra category hay không
        if instance.created_by != request.user:
            return Response({"error": "You do not have permission to delete this book"},
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)