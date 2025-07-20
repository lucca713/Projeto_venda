import pymongo
from django.conf import settings

# Estabelece conexao com o Mongo DB

def get_mongo_collection():
    try:
        client = pymongo.MongoClient(settings.MONGO_CONNECTION_STRING)
        db = client[settings.MONGO_DATABASE_NAME]
        collection = db[settings.MONGO_COLLECTION_NAME]
    # Testa se a conexão está ativa
        client.admin.command('ping') 
        print("Conexão com MongoDB bem-sucedida.")
        return collection
    except Exception as e:
        print(f"conexao falhou :(")
        return None
# Vai receber do nova_venda e coloar em um json para conseguir colocar no mongoDB
def salvar_venda_no_mongo(venda_obj_sql):

    collection = get_mongo_collection()
    if collection is None:
        print("Operação no MongoDB cancelada devido à falha na conexão.")
        return

    # Monta dicionario
    venda_documento = {
        "venda_id_sql": venda_obj_sql.id,
        "comprador_id": venda_obj_sql.comprador.id,
        "comprador_nome": venda_obj_sql.comprador.nome,
        "data_venda": venda_obj_sql.data_venda,
        "subtotal": float(venda_obj_sql.subtotal),
        "endereco_entrega": {
            "cep": venda_obj_sql.cep,
            "rua": venda_obj_sql.rua,
            "bairro": venda_obj_sql.bairro,
            "cidade": venda_obj_sql.cidade,
            "estado": venda_obj_sql.estado,
        },
        "itens": []
    }

    #  adiciona no dicionario

    for item_sql in venda_obj_sql.itens.all():
        venda_documento["itens"].append({
            "produto_id_sql": item_sql.produto.id,
            "produto_nome": item_sql.produto.nome,
            "quantidade": item_sql.quantidade,
            "preco_unitario": float(item_sql.preco_unitario),
            "fornecedores": [f.nome for f in item_sql.produto.fornecedores.all()]
        })

    # Insere o documento no mongoDB
    try:
        collection.insert_one(venda_documento)
        print(f"Venda #{venda_obj_sql.id} copiada para o MongoDB com sucesso.")
    except Exception as e:
        print(f" Erro ao inserir venda #{venda_obj_sql.id} no MongoDB: {e}")