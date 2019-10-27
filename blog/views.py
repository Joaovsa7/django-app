from django.shortcuts import render,get_object_or_404
from .forms import ComentarioForm
from .models import Postagem
# Create your views here.

def post_list(request):
    postagem = Postagem.objects.filter(status=1).order_by('-criado_em')
    context = {
        'object': postagem
    }
    return render(request, '../templates/index.html', context)

def post_detail(request,slug):
    postagem = get_object_or_404(Postagem,slug=slug)
    comentarios = postagem.comentarios.filter(ativo=True)
    novoComentario = None
    # Quando o comentário for postado
    if request.method == 'POST':
        formularioDeComentario = ComentarioForm(data=request.POST)
        if formularioDeComentario.is_valid():
            novoComentario = formularioDeComentario.save(commit=False)
            novoComentario.postagem = postagem
            novoComentario.save()
    
    else:
        formularioDeComentario = ComentarioForm()
        
    context = {
        'post': postagem,
        'comentarios': comentarios,
        'novo_comentario': novoComentario,
        'coment_form': formularioDeComentario
    }
    template = '../templates/post_detail.html'
    return render(request, template,context)
