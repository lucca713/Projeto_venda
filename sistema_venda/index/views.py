from django.shortcuts import render
from .models import Comprador, Produto

def nova_venda(request):
    #passar produto e comprador para poder listar no select
    compradores = Comprador.objects.all()
    produtos = Produto.objects.all()

    context = {
        'compradores': compradores,
        'produtos': produtos
    }

    return render(request, './nova_venda.html', context) #arrumar esse caminho dps