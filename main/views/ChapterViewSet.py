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
        return Chapter.objects.filter(book_id=book_id)
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)
