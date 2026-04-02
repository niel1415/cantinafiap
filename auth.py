from dados import USUARIOS


def autenticar(login, senha):
    for usuario in USUARIOS:
        if usuario["login"] == login and usuario["senha"] == senha:
            return usuario
    return None