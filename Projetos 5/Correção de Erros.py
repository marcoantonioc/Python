try:
    a=int(input('Indique um numero :'))
    b=int(input('Indique um numero :'))
    r=a/b
except ZeroDivisionError:
    print(f"Não é possivel dividir o numero por zero !")
except ValueError:
    print(f"Não sei o que isto faz !")
else:
    print(f'O resultado é {r}')
finally:
    print(f"Volte sempre")