from django.db import models
# colocar modelo de negocio: cada classe vai ser uma tabela do banco: 

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=12, decimal_places=2)

    #relacao entre produto e forncedor

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
    