from ex115a.lib.interface import *

def ArquivoExiste(nome):
    try:
        a=open(nome,'rt') # read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a=open(nome,'wt+') # write text , criar
    except:
        print('Houve Algum erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso !')


def lerarquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado=linha.split(';')
            dado[1].replace('\n',"")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()
def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a=open(arq,'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print('houve um ERRO na hora de escrever os dados')
        else:
            print(f"Novo registro de {nome} adicionado !")
            a.close()