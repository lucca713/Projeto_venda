from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404 #para retornar o erro
from django.db import transaction
from .models import Comprador, Produto, Venda, Itemvenda
from . import utils
import json

#configurando os dados enviados para o banco
def index(request):
     return render(request,'./index.html')
    


def nova_venda(request):
    
    if request.method == 'POST':

        # Iniciando variavel que vai guardar a venda feita para copiar do Postegre para o Mongo
        venda_salva_sql = None

        #processa o formulario 
        try:
            comprador_id = request.POST.get('comprador')
            cep = request.POST.get('cep')
            rua = request.POST.get('rua')
            bairro = request.POST.get('bairro')
            cidade = request.POST.get('cidade')
            estado = request.POST.get('estado')

            #pega itens do campo hidden (estao em json)

            itens_json = request.POST.get('itens_venda')
            itens = json.loads(itens_json)

            #caso nenhum item estiver avenda(nunca vai cair aqui pois vou adicionar no admin) -> tratativa de erro
            if not itens:
                raise ValueError("Nenhum item esta sendo vendido - acabou estoque :(")
            
            comprador = Comprador.objects.get(id=comprador_id)

            #aqui vou garantir que a venda e itens sejam salvas juntas

            with transaction.atomic():
                #objeto venda
                venda = Venda.objects.create(comprador=comprador, cep=cep, rua=rua, bairro=bairro, cidade=cidade, estado=estado)

                subtotal_calculado = 0

                #objeto ItemVenda

                for item_data in itens:
                    produto = Produto.objects.get(id= item_data['produto_id'])
                    Itemvenda.objects.create(
                        venda=venda,
                        produto=produto,
                        quantidade=item_data['quantidade'],
                        preco_unitario=item_data['preco_unitario']
                    )
                    subtotal_calculado += float(item_data['subtotal'])
                
                # A VENDA VAI GUARDAR EM AMBOS OS BANCOS
                
                #atualizar o subtotal da venda
                venda.subtotal = subtotal_calculado
                venda.save()

                # Guardando Venda nela
                venda_salva_sql = venda

            if venda_salva_sql:
                try:
                    utils.salvar_venda_no_mongo(venda_salva_sql)
                except Exception as e:
                    print('nao deu certo salvar no mongoDB :( {e}') 
               
            #levar para a página de sucesso
            return redirect('sucesso')

        except Exception as e:
            print(f"Erro ao processar a venda: {e}")

            #recarregar a pagina para corrigir

            compradores = Comprador.objects.all()
            produtos = Produto.objects.all()
            context = {
                'compradores': compradores,
                'produtos': produtos,
                'error': 'Ocorreu um erro ao salvar a venda. Verifique os dados.'
            }
            return render(request, './nova_venda.html', context)
    else:
        compradores = Comprador.objects.all()
        produtos = Produto.objects.all()
        context = {
            'compradores': compradores,
            'produtos': produtos,
        }
        return render(request, './nova_venda.html', context)


def pagina_sucesso(request):
    return render(request, './sucesso.html')
                    
                
def lista_produto(request):
    # Pegar o q da query, depois do "q" vai estar o produto na url
    query = request.GET.get('q')

    if query:
        # Filtrar produto
        produto = Produto.objects.filter(nome__icontains=query)
    else:
        #lista todos se nao tiver
        produto = Produto.objects.all()

    return render(request, './lista_produtos.html', {'produtos': produto})

#Somente o mongo vai receber o historico 

def historico_compras(request, comprador_id):
   
    comprador = get_object_or_404(Comprador, id=comprador_id)
    vendas_do_mongo = []
    
    collection = utils.get_mongo_collection()
    
    if collection is not None:
        
        cursor = collection.find(
            {'comprador_id': comprador_id}
        ).sort('data_venda', -1)
        
        vendas_do_mongo = list(cursor)

    context = {
        'comprador': comprador,
        'vendas': vendas_do_mongo
    }
    return render(request, './historico_compras.html', context)

def lista_clientes(request):
    #pegar todos os clientes

    comprador = Comprador.objects.all().order_by('nome')
    context = {
        'compradores':comprador,
    }
    return render(request,'./lista_clientes.html', context)

def lista_clientes_only(request):
    #pegar todos os clientes

    comprador = Comprador.objects.all().order_by('nome')
    context = {
        'compradores':comprador,
    }
    return render(request,'./lista_clientes_only.html', context)




'''
def historico_compras(request, comprador_id):
    comprador = get_object_or_404(Comprador, id= comprador_id)

    #Filtrar venda pelo mais recente

    vendas = Venda.objects.filter(comprador=comprador).order_by('-data_venda')

    context = {
        'comprador':  comprador,
        'vendas': vendas,
    }
    return render(request, './historico_compras.html', context)
'''


