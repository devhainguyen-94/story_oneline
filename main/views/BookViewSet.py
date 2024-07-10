from rest_framework import generics
from main.models import Book ,Category
from main.serializers import BookSerializer , CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins , viewsets
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
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

    def test(self, request=None):
        try:
            # Lấy ra đối tượng Book từ cơ sở dữ liệu dựa trên book_id
            book_id = request.query_params.get('book_id')
            book = Book.objects.get(pk=book_id)

            # Sử dụng một Serializer để serialize các category của cuốn sách
            serializer = CategorySerializer(book.category.all(), many=True)

            # Chuyển đổi kết quả thành chuỗi JSON
            json_data = JSONRenderer().render(serializer.data)

            # In ra chuỗi JSON hoặc trả về nó như là một phản hồi JSON
            print(json_data)
            return JsonResponse(serializer.data, safe=False)  # Sử dụng JsonResponse để trả về JSON
        except Book.DoesNotExist:
            return HttpResponse(f"Book with ID {book_id} does not exist", status=404)
        # book = Book.objects.filter(pk=19)
        # print(book.category)
        # for obj in book:
        #     # Xử lý mỗi đối tượng ở đây
        #     print(obj)
