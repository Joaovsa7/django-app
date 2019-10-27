from django.shortcuts import render, get_object_or_404
from .models import Postagem
# Create your views here.

def post_list(request):
    postagem = Postagem.objects.filter(status=1).order_by('-criado_em')
    context = {
        'object': postagem
    }
    return render(request, '../templates/index.html', context)

def post_detail(request, pk):
    postagem = get_object_or_404(Postagem, pk=pk)
    context = {
        'post': postagem,
    }
    return (request, '../templates/post_detail.html', context)
