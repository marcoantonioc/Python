#Funções em Python é uma rotina ,
#def mostralinha():
    #print("="*35)


#mostralinha()
#print(" HELLO WORLD")
#mostralinha()

#def mensagem(msg):
    #print("-="*35)
    #print(msg)
    #print("-="*35)
    #print()


#mensagem("HELLO WORD")
#mensagem("Vai de fuder")
#mensagem("DEDSEC")


#def conta(a,b):
    #print(f"A= {a} + B= {b}")
    #s=a+b
    #print(f"A+b={s}")


#conta(2,3)
#conta(a=4,b=5)


#def contador(*num):
    #for valor in num:
        #print(f"{valor}",end="")
        #print()
#contador(2,4,5,1,'marco')
#contador('luca',"marco",'mariana','ruslan')


#def dobra(lst):
    #pos=0
    #while pos < len(lst):
        #lst[pos] *= 2
        #pos+1


#valores=(2, 5, 7, 2, 4, 8)
#dobra(valores)

#print(valores)


#====================================================================================
#     FUNÇÕES PARTE 2

# Este comando printa o manual do função (É melhor usar em console)
#help(print ou len ou def)
# OU
# print(input.__doc__)

#def contador(i,f,p):
    #"""
    #Ola luca seu gay
    #"""

    #while i<=f:
        #print(f"{i}",end="..")
        #i+=p
    #print("FIM")

#help(contador)

#Crias um manual Proprio

#=================
#def somar(a,b,c=0):
    #s=a+b+c
    #print(f"A soma é {s}")
#somar(5,3)
#Se não for informado o valor de c , ele será zero como indicado

#===========
#def num(b):
    #global a #--> Este há é o mesmo a , é o a global
    #a=8
    #b+=4
    #c=2
    #print(f"O A aqui é global é {a} ")
    #print(f"O B tem o valor de {b}")
#a=5
#print(f"O A de fora é {a}")
#num(a)

def soma(a=0,b=0,c=0):
    s=a+b+c
    return s
r1=soma(3,4,5)
r2=soma(6,2)
print(f"Os resultados foram {r1} {r2}")








