from django.urls import path
from . import views
from .views import RegisterView, CustomTokenObtainPairView

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('comments/', views.CommentsListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>', views.CommentDetailView.as_view(), name='comment-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_ pair'),
]