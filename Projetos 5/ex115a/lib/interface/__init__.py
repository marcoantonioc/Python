def leiaint(num):
    while True:
        try:
            n=int(input(num))
        except ValueError:
            print(f"Erro valor inválido!")
            continue
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção:\033[m')
    return opc


def organizar(nome,idade):
    print(f"{nome}    {idade} anos")