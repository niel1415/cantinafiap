from auth import autenticar
from pedidos import (
    exibir_cardapio,
    buscar_item_cardapio,
    criar_pedido,
    listar_pedidos_aluno,
    cancelar_pedido,
    listar_todos_pedidos,
    atualizar_status_pedido,
    calcular_total
)


def menu_aluno(usuario):
    carrinho = []

    while True:
        print(f"\n=== MENU ALUNO | {usuario['nome']} ===")
        print("1 - Ver cardápio")
        print("2 - Adicionar item ao carrinho")
        print("3 - Remover item do carrinho")
        print("4 - Ver carrinho")
        print("5 - Finalizar pedido")
        print("6 - Meus pedidos")
        print("7 - Cancelar pedido")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_cardapio()

        elif opcao == "2":
            exibir_cardapio()
            try:
                item_id = int(input("Digite o ID do item: "))
                item = buscar_item_cardapio(item_id)
                if item:
                    carrinho.append(item)
                    print(f'{item["nome"]} adicionado ao carrinho.')
                else:
                    print("Item inválido ou indisponível.")
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "3":
            if not carrinho:
                print("Carrinho vazio.")
            else:
                print("\n=== CARRINHO ===")
                for i, item in enumerate(carrinho, start=1):
                    print(f'{i} - {item["nome"]} | R$ {item["preco"]:.2f}')
                try:
                    indice = int(input("Digite o número do item para remover: "))
                    if 1 <= indice <= len(carrinho):
                        removido = carrinho.pop(indice - 1)
                        print(f'{removido["nome"]} removido do carrinho.')
                    else:
                        print("Item inválido.")
                except ValueError:
                    print("Digite um número válido.")

        elif opcao == "4":
            if not carrinho:
                print("Carrinho vazio.")
            else:
                print("\n=== CARRINHO ===")
                for item in carrinho:
                    print(f'- {item["nome"]} | R$ {item["preco"]:.2f}')
                print(f'Total: R$ {calcular_total(carrinho):.2f}')

        elif opcao == "5":
            criar_pedido(usuario, carrinho)
            carrinho = []

        elif opcao == "6":
            listar_pedidos_aluno(usuario["nome"])

        elif opcao == "7":
            try:
                pedido_id = int(input("Digite o número do pedido que deseja cancelar: "))
                cancelar_pedido(usuario["nome"], pedido_id)
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "0":
            print("Saindo do menu do aluno...")
            break

        else:
            print("Opção inválida.")


def menu_atendente(usuario):
    while True:
        print(f"\n=== MENU ATENDENTE | {usuario['nome']} ===")
        print("1 - Ver todos os pedidos")
        print("2 - Atualizar status de pedido")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_todos_pedidos()

        elif opcao == "2":
            try:
                pedido_id = int(input("Digite o número do pedido: "))
                print("Status possíveis: Recebido, Em preparo, Pronto, Entregue")
                novo_status = input("Digite o novo status: ").strip()
                atualizar_status_pedido(pedido_id, novo_status)
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "0":
            print("Saindo do menu do atendente...")
            break

        else:
            print("Opção inválida.")


def main():
    print("=== CANTINAFIAP ===")
    print("Sistema de pedidos na cantina\n")

    while True:
        login = input("Login: ")
        senha = input("Senha: ")

        usuario = autenticar(login, senha)

        if usuario:
            print(f'\nBem-vindo, {usuario["nome"]}!')
            if usuario["perfil"] == "aluno":
                menu_aluno(usuario)
            else:
                menu_atendente(usuario)

            sair = input("\nDeseja encerrar o sistema? (s/n): ").lower()
            if sair == "s":
                print("Sistema encerrado.")
                break
        else:
            print("Login ou senha inválidos.\n")


if __name__ == "__main__":
    main()