import json
import os

ARQUIVO_PEDIDOS = "pedidos.json"


def carregar_pedidos():
    if not os.path.exists(ARQUIVO_PEDIDOS):
        return []

    try:
        with open(ARQUIVO_PEDIDOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return []


def salvar_pedidos(pedidos):
    with open(ARQUIVO_PEDIDOS, "w", encoding="utf-8") as arquivo:
        json.dump(pedidos, arquivo, ensure_ascii=False, indent=4)


def gerar_novo_id(pedidos):
    if not pedidos:
        return 1
    return max(pedido["id"] for pedido in pedidos) + 1