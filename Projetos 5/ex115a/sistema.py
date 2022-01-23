from ex115a.lib.interface import *
from ex115a.lib.arquivo import *
from time import sleep

arq='arquivo_nomes.txt'

if not ArquivoExiste(arq):
    criararquivo(arq)

while True:
    resposta=menu(['Lista de Pessoas','Cadastrar Pessoas','Sair'])
    if resposta==1:
        # OPÇÃO DE MOSTRAR O ARQUIVO
        lerarquivo(arq)
    elif resposta==2:
        cabeçalho('NOVO CADASTRO')
        nome=str(input('Nome:'))
        idade=leiaint('Idade:')
        cadastrar(arq,nome,idade)
    elif resposta==3:
        cabeçalho("Saindo do Sistema!")
        break
    else:
        print('\033[31mOpcao Invalida \033[m')
    sleep(2)

