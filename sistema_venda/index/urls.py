from django.urls import path
from . import views

urlpatterns = [
    #Leva para a tela de nova venda
    path('', views.index, name='index'),

    path('nova_venda/', views.nova_venda, name='nova_venda'),

    path('clientesOnly/', views.lista_clientes_only, name='lista_clientes_only'),

    #Sucesso ao eviar o forms
    path('/sucesso', views.pagina_sucesso, name='sucesso'),

    #Tela de lista dos produtos
    path('produtos/', views.lista_produto, name='lista_produtos'),

    #Tela do relatório das vendas
    path('historico/<int:comprador_id>/', views.historico_compras, name='historico_compras'),

    path('clientes/', views.lista_clientes, name='lista_clientes'),

]