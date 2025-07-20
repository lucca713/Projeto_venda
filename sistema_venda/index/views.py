from django.shortcuts import render, redirect
from django.db import transaction
from .models import Comprador, Produto, Venda, Itemvenda
import json
#configurando os dados enviados para o banco
def nova_venda(request):
    if request.method == 'POST':

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
                
                #atualizar o subtotal da venda
                venda.subtotal = subtotal_calculado
                venda.save()

            #levar para a página de sucesso
            return redirect('sucesso')
        
        except Exception as e:
            print(f"Erro ao processar a venda: {e}")

            #recarregar a pagina para corrigir

            compradores = Comprador.objects.all()
            produto= Produto.objects.all()
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


                    
                




