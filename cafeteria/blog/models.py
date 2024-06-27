# models.py

from django.db import models
from django.utils.html import format_html

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')

    def image_tag(self):
        return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />'.format(self.image.url))

    image_tag.short_description = 'Imagen'
