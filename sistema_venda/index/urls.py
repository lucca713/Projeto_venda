from django.urls import path
from . import views

urlpatterns = [
    #Leva para a tela de nova venda
    path('', views.nova_venda, name='nova_venda'),

    #Sucesso ao eviar o forms
    path('/sucesso', views.pagina_sucesso, name='sucesso'),

    #Tela de lista dos produtos
    path('produtos/', views.lista_produto, name='lista_produtos'),

    #Tela do relatório das vendas
    path('historico/<int:comprador_id>/', views.historico_compras, name='historico_compras'),
]