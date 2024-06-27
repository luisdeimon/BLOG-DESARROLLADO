# admin.py

from django.contrib import admin
from .models import Post, Image
from django.utils.html import format_html

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image_preview', 'image_tag')
    readonly_fields = ('image_preview', 'image_tag',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        else:
            return '(Sin imagen)'
    image_preview.short_description = 'Vista previa de la imagen'

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />', obj.image.url)
        else:
            return '(Sin imagen)'
    image_tag.short_description = 'Imagen'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at_formatted', 'preview_content_with_spacing', 'images_preview')
    readonly_fields = ('created_at',)
    inlines = [ImageInline]

    def created_at_formatted(self, obj):
        return obj.created_at.strftime("%d %b %Y %H:%M:%S")
    created_at_formatted.short_description = 'Created at'

    def preview_content_with_spacing(self, obj):
        return format_html('<div style="white-space: pre-line;">{}</div>', obj.content)
    preview_content_with_spacing.short_description = 'Content'

    def images_preview(self, obj):
        images_html = ''
        for image in obj.images.all():
            images_html += f'<img src="{image.image.url}" style="max-height: 100px; max-width: 100px; margin-right: 10px;" />'
        return format_html(images_html)
    images_preview.short_description = 'Images'
    images_preview.allow_tags = True

admin.site.register(Post, PostAdmin)
admin.site.register(Image)
