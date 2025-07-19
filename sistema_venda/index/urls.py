from django.urls import path
from . import views

urlpatterns = [
    #leva para a tela de nova venda
    path('', views.nova_venda, name='nova_venda')
]