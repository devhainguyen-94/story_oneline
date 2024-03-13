from django.urls import path ,include
from rest_framework_simplejwt import views as jwt_views
# from . import views
from .views import CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
router = DefaultRouter()
# router.register(r'category', CategoryViewSet, basename='category')
urlpatterns = [
      path('', include(router.urls)),
      path('category/', CategoryViewSet.CategoryListCreateAPIView.as_view(), name='category-list-create'),
      path('category/<int:pk>/', CategoryViewSet.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
      path('category/<int:category_id>/', CategoryViewSet.CategoryDeleteAPIView.as_view(), name='category-delete'),
      path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/register/', register_user, name='register'),
      # path('api-auth/', include('rest_framework.urls')),
]

# urlpatterns = format_suffix_patterns(urlpatterns)