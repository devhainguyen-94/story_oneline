from rest_framework import mixins , viewsets ,renderers ,permissions
# from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL


# from serializers import CategorySerialzer
from main.models import Category 
from main.serializers import CategorySerializer
class CategoryViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    authentication_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)
<<<<<<< HEAD

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
=======
    def save(self, *args ,**kwargs):
        return 1
    def perform_create(self, serializer):
        userCustomer=CategorySerializer(data = serializer)
        if userCustomer.is_valid():
            userCustomer.create(created_by=self.request.user)
>>>>>>> 8cdfbfc (category)
