from django.db import models
# colocar modelo de negocio: cada classe vai ser uma tabela do banco: 

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
   
    #relacao entre produto e forncedor -> cria uma tabela nova para essa relacao
    fornecedores = models.ManyToManyField(Fornecedor)

    def __str__(self):
        return f"{self.nome} - R${self.valor}"
    
class Comprador(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome    
    
class Venda(models.Model):
    
    comprador = models.ForeignKey(Comprador, on_delete=models.PROTECT)
    data_venda = models.DateTimeField(auto_now=True)

    #endereco

    cep = models.CharField(max_length=12)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)

    def __str__(self):
        return f"venda {self.id} - {self.Comprador.nome}" #pega o nome por conta da ForeignKey

class Itemvenda(models.Model):
    #relacao de venda e produto, o mesmo produto pode ter varias vendas

    venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)#tudo filtrado pelo itens.all()
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveBigIntegerField(default=1)

    #preco produto na hora da venda(para manter o historico correto)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} na venda {self.venda.id}"
    