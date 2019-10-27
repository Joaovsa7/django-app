from django.db import models
from django.contrib.auth.models import  User
from tinymce.models import HTMLField

STATUS = (
    (0, "RASCUNHO"),
    (1, "PUBLICADO")
)

class Postagem(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_postagens')
    conteudo = HTMLField()
    atualizado_em = models.DateTimeField(auto_now= True)
    criado_em = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios')
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    body = HTMLField()
    criado_em = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['criado_em']
    
    def __str__(self):
        return 'Comentário {} por {}'.format(self.body, self.nome)
    