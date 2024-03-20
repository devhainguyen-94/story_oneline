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
        serializer.save(auth_id = self.request.user)
