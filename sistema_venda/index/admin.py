from django.contrib import admin

# importando as tabelas 
from .models import Fornecedor, Produto, Comprador, Venda, Itemvenda

#para visualizar os iten que vao ser vendidos dentro do proprio administrador

class ItemVendaInLine(admin.TabularInline):
    model = Itemvenda
    extra = 1

@admin.register(Venda)
class vendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInLine]
    list_display = ('id', 'comprador', 'data_venda', 'subtotal')
    readonly_fields = ('subtotal',)  
    
#registrar outros modelos 
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Comprador)