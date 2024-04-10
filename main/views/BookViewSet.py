from rest_framework import generics
from main.models import Book
from main.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins , viewsets

class BookListCreateAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(auth = self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request)
        # Kiểm tra xem người dùng hiện tại có phải là người tạo ra category hay không
        if instance.created_by != request.user:
            return Response({"error": "You do not have permission to delete this book"},
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)