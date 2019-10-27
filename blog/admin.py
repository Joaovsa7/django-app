from django.contrib import admin
from .models import Postagem, Comentario

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'status','criado_em')
    list_filter = ("status",)
    search_fields = ['titulo', 'conteudo']
    prepopulated_fields = {'slug': ('titulo',)}
    
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('postagem', 'nome', 'ativo', 'criado_em', 'body')
    list_filter = ('ativo', 'criado_em')
    search_fields = ['postagem', 'nome', 'email', 'criado_em', 'ativo']
    actions = ['aprova_comentario']
    
    def aprova_comentario(self, request, queryset):
        queryset.update(ativo=True)

admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Postagem, PostAdmin)
