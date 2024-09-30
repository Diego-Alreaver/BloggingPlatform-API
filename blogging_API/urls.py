from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path('blogging_API/', PostListCreateView.as_view(), name='post-list-create'),  # GET y POST para listar y crear posts
    path('blogging_API/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # GET, PUT y DELETE para detalles del post
]