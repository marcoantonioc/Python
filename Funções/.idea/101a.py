def voto(num=0):
    from datetime import date
    data=date.today().year
    idade =  data-num
    if idade<16:
       return f"Voce tem {idade} e o voto é NEGADO"
    elif 16<= idade <18 or idade>65:
       return f"Voce tem {idade} e o voto é opcional"
    else:
       return f"Voce tem {idade} anos e o voto é OBRIGATÓRIO"


nas=int(input("Indique o ano em que nasceu : "))

print(voto(nas))