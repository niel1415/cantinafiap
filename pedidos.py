from datetime import datetime
from dados import CARDAPIO
from utils import carregar_pedidos, salvar_pedidos, gerar_novo_id


def exibir_cardapio():
    print("\n=== CARDÁPIO ===")
    for item in CARDAPIO:
        status = "Disponível" if item["disponivel"] else "Indisponível"
        print(f'{item["id"]} - {item["nome"]} | R$ {item["preco"]:.2f} | {status}')


def buscar_item_cardapio(item_id):
    for item in CARDAPIO:
        if item["id"] == item_id and item["disponivel"]:
            return item
    return None


def calcular_total(carrinho):
    return sum(item["preco"] for item in carrinho)


def criar_pedido(usuario, carrinho):
    pedidos = carregar_pedidos()

    if not carrinho:
        print("Carrinho vazio. Não é possível finalizar o pedido.")
        return

    novo_pedido = {
        "id": gerar_novo_id(pedidos),
        "aluno": usuario["nome"],
        "itens": carrinho,
        "total": calcular_total(carrinho),
        "status": "Recebido",
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    pedidos.append(novo_pedido)
    salvar_pedidos(pedidos)

    print("\nPedido realizado com sucesso!")
    print(f'Número do pedido: {novo_pedido["id"]}')
    print(f'Total: R$ {novo_pedido["total"]:.2f}')


def listar_pedidos_aluno(nome_aluno):
    pedidos = carregar_pedidos()
    encontrados = [p for p in pedidos if p["aluno"] == nome_aluno]

    if not encontrados:
        print("\nVocê ainda não possui pedidos.")
        return

    print("\n=== MEUS PEDIDOS ===")
    for pedido in encontrados:
        print(f'\nPedido #{pedido["id"]}')
        print(f'Status: {pedido["status"]}')
        print(f'Data/Hora: {pedido["data_hora"]}')
        print("Itens:")
        for item in pedido["itens"]:
            print(f'- {item["nome"]} | R$ {item["preco"]:.2f}')
        print(f'Total: R$ {pedido["total"]:.2f}')


def cancelar_pedido(nome_aluno, pedido_id):
    pedidos = carregar_pedidos()

    for pedido in pedidos:
        if pedido["id"] == pedido_id and pedido["aluno"] == nome_aluno:
            if pedido["status"] in ["Em preparo", "Pronto", "Entregue"]:
                print("\nNão é possível cancelar esse pedido devido ao status atual.")
                return
            pedido["status"] = "Cancelado"
            salvar_pedidos(pedidos)
            print("\nPedido cancelado com sucesso.")
            return

    print("\nPedido não encontrado.")


def listar_todos_pedidos():
    pedidos = carregar_pedidos()

    if not pedidos:
        print("\nNenhum pedido foi realizado ainda.")
        return

    print("\n=== TODOS OS PEDIDOS ===")
    for pedido in pedidos:
        print(f'\nPedido #{pedido["id"]}')
        print(f'Aluno: {pedido["aluno"]}')
        print(f'Status: {pedido["status"]}')
        print(f'Data/Hora: {pedido["data_hora"]}')
        print("Itens:")
        for item in pedido["itens"]:
            print(f'- {item["nome"]} | R$ {item["preco"]:.2f}')
        print(f'Total: R$ {pedido["total"]:.2f}')


def atualizar_status_pedido(pedido_id, novo_status):
    pedidos = carregar_pedidos()
    status_validos = ["Recebido", "Em preparo", "Pronto", "Entregue"]

    if novo_status not in status_validos:
        print("\nStatus inválido.")
        return

    for pedido in pedidos:
        if pedido["id"] == pedido_id:
            pedido["status"] = novo_status
            salvar_pedidos(pedidos)
            print("\nStatus atualizado com sucesso.")
            return

    print("\nPedido não encontrado.")