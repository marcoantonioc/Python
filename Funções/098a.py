def contar(inicio,final,passo):

    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    if inicio > final:
        passo = passo - (passo * 2)

        for i in range(inicio,final+passo,passo):
            print(f"{i}_",end="")

    if final>inicio:
        for i in range(inicio,final,passo):
            print(f"{i}_",end="")

        print()
        print("="*30)


contar(1,10,1)
contar(10,0,2)

print("Agora é a sua vez de personalizar a contagem: ")

ini=int(input("Inicio: "))
fim=int(input("Final: "))
pas=int(input("Passo: "))

contar(ini,fim,pas)