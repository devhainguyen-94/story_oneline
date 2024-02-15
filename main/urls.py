from django.urls import path
from rest_framework_simplejwt import views as jwt_views
# from . import views
from .views import CategoryViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
# urlpatterns = [
#     path('test', views.index, name='index'),
#     path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/register/', register_user, name='register'),
# ]