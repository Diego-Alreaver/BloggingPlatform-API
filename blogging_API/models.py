from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)  # Título del blog
    content = models.TextField()  # Contenido del blog
    category = models.CharField(max_length=100)  # Categoría del blog
    tags = models.CharField(max_length=255)  # Tags del blog como string separado por comas
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización

    def __str__(self):
        return self.title