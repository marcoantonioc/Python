pessoa=dict()
from datetime import date
data=date.today().year

pessoa['nome']=str(input("Indique o seu nome: "))

nascimento=int(input("Indique o ano de nascimento: "))
idade= data-nascimento
pessoa['idade']=idade

pessoa['carteira']=int(input("Indique a sua carteia de trabalho (0 não tem): "))
if pessoa['carteira']!=0:
    pessoa['contradado'] =int(input("Ano de contratação: "))

    pessoa['aposentadoria']=idade+(pessoa['contradado']+35)-data

    pessoa['salario']=float(input("INdique o seu salario: "))
    print("=" * 30)

    for k, v in pessoa.items():
        print(f"No campo {k} tem o valor {v}")






