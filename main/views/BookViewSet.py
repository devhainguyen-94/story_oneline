from rest_framework import generics
from main.models import Book ,Category
from main.serializers import BookSerializer , CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins , viewsets
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
import gtts
from pydub import AudioSegment
import cloudinary.uploader
import cloudinary
import os
from django.conf import settings
cloudinary.config(
  cloud_name = "dwtcdblb7",
  api_key = "696585576229197",
  api_secret = "jv3B694lhlR5yGQx3oTB5iWzvn8"
)
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
            return HttpResponse({"error": "You do not have permission to delete this book"},
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        # return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return HttpResponse(f"Book deleted successfully")
    def test(self, request=None):
        try:
            # Lấy ra đối tượng Book từ cơ sở dữ liệu dựa trên book_id
            t1 = gtts.gTTS(text="t là máy đọc truyện  " , lang='vi' )
            t1.save("upload/welcome.mp3")
            # playsound("welcome.mp3")

            # # Tải các tệp MP3
            main_audio = AudioSegment.from_file("welcome2.mp3")
            background_music = AudioSegment.from_file("nhacnen.mp3")

            # Điều chỉnh âm lượng của nhạc nền
            background_music = background_music - 5  # Giảm âm lượng nhạc nền xuống 20dB

            # Lặp lại nhạc nền cho đến khi bằng độ dài của tệp chính
            background_music = background_music * (len(main_audio) // len(background_music) + 1)

            # Cắt nhạc nền sao cho có độ dài bằng với tệp chính
            background_music = background_music[:len(main_audio)]

            # Trộn nhạc nền vào tệp chính
            combined = main_audio.overlay(background_music)

            # Xuất tệp âm thanh kết hợp
            # combined.export("output_with_background2.mp3", format="mp3")
            # output_path = "output_with_background2.mp3"
            output_path2 = os.path.join(settings.BASE_DIR, "upload/output_with_background2.mp3")
            combined.export(output_path2, format="mp3")

            # Đảm bảo file đã được lưu thành công trước khi upload
            if os.path.exists(output_path2):
                result = cloudinary.uploader.upload(output_path2, resource_type="video")
                cloudinary_url = result.get('url')
                return HttpResponse(f"File uploaded successfully! URL:{output_path2} ")
            else:
                return HttpResponse("Error: File not found", status=500)
            result = cloudinary.uploader.upload(output_path, resource_type="video")
            cloudinary_url = result['url']  # Lấy URL của file trên Cloudinary
            # return HttpResponse(f"File uploaded successfully! URL: {cloudinary_url}")
        except Book.DoesNotExist:
            return HttpResponse(f"Book with ID {book_id} does not exist", status=404)
        # book = Book.objects.filter(pk=19)
        # print(book.category)
        # for obj in book:
        #     # Xử lý mỗi đối tượng ở đây
        #     print(obj)
    # def test(self, request=None):
    #     try:
    #         # Tạo file MP3 với gTTS
    #         t1 = gtts.gTTS(text="t là máy đọc truyện", lang='vi')
    #         t1.save("upload/welcome.mp3")

    #         # Tải các tệp MP3
    #         main_audio = AudioSegment.from_file("upload/welcome.mp3")
    #         background_music = AudioSegment.from_file("nhacnen.mp3")

    #         # Điều chỉnh âm lượng của nhạc nền
    #         background_music = background_music - 5  # Giảm âm lượng nhạc nền xuống 5dB

    #         # Lặp lại nhạc nền cho đến khi bằng độ dài của tệp chính
    #         background_music = background_music * (len(main_audio) // len(background_music) + 1)

    #         # Cắt nhạc nền sao cho có độ dài bằng với tệp chính
    #         background_music = background_music[:len(main_audio)]

    #         # Trộn nhạc nền vào tệp chính
    #         combined = main_audio.overlay(background_music)

    #         # Xuất tệp âm thanh kết hợp
    #         output_path = "upload/output_with_background2.mp3"
    #         combined.export(output_path, format="mp3")

    #         # Tải tệp lên Cloudinary
    #         # result = cloudinary.uploader.upload(output_path, resource_type="video")
    #         # cloudinary_url = result['url']  # Lấy URL của file trên Cloudinary

    #         return HttpResponse(f"File uploaded successfully! URL: 123")
    #     except Exception as e:
    #         # Đảm bảo trả về HttpResponse ngay cả khi có lỗi
    #         return HttpResponse(f"An error occurred: {e}", status=500)