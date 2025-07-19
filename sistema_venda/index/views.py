from django.shortcuts import render
from .models import Comprador, Produto

def nova_venda(request):
    #passar produto e comprador para poder listar no select
    compradores = Comprador.objects.all()
    produto = Produto.objects.all()

    context = {
        'compradores': compradores,
        'produto': produto
    }

    return render(request, './nova_venda', context) #arrumar esse caminho dps