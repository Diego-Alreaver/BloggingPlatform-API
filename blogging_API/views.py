from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(APIView):
    def get(self, request):
        term = request.query_params.get('term', None)
        if term:
            posts = Post.objects.filter(
                title__icontains=term
            ) | Post.objects.filter(
                content__icontains=term
            ) | Post.objects.filter(
                category__icontains=term
            )
        else:
            posts = Post.objects.all()
        if not posts.exists():
            return Response({"message": "No se encontraron posts con ese término de búsqueda."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Crear un nuevo post
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    def get(self, request, pk):
        # Obtener un post específico
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        # Actualizar un post existente
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Eliminar un post
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)