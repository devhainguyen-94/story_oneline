from rest_framework import generics
from main.models import Chapter
from main.serializers import ChapterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins , viewsets

class ChapterListCreateAPIView(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book_id = self.request.query_params.get('book_id')
        if book_id:
            return Chapter.objects.filter(book_id=book_id)
        return Chapter.objects.all()
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request)
        # Kiểm tra xem người dùng hiện tại có phải là người tạo ra category hay không
        if instance.created_by != request.user:
            return Response({"error": "You do not have permission to delete this Book"},
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)