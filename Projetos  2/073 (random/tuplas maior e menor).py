from random import randint

maior=0
menor=0


tupla=(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
print(tupla)

print(f'O maior numero foi {max(tupla)}, e o menor numero foi {min(tupla)}')

# OU

#if tupla[0] > tupla[1] and tupla[0] > tupla[2] and tupla[0] > tupla[3] and tupla[0] > tupla[4] :
    #maior=tupla[0]
    #menor=tupla[0]
#elif tupla[1] > tupla[0] and tupla[1] > tupla[2] and tupla[1] > tupla[3] and tupla[1] > tupla[4] :
    #maior=tupla[1]
    #menor = tupla[1]
#elif tupla[2] > tupla[0] and tupla[2] > tupla[1] and tupla[2] > tupla[3] and tupla[2] > tupla[4] :
    #maior=tupla[2]
    #menor = tupla[2]
#elif tupla[3] > tupla[0] and tupla[3] > tupla[2] and tupla[3] > tupla[1] and tupla[3] > tupla[4] :
    #maior=tupla[3]
    #menor = tupla[3]
#elif tupla[4] > tupla[0] and tupla[4] > tupla[2] and tupla[4] > tupla[3] and tupla[4] > tupla[1] :
    #maior=tupla[4]
    #menor = tupla[4]
#menor numero
#if tupla[0] < tupla[1] and tupla[0] < tupla[2] and tupla[0] < tupla[3] and tupla[0] < tupla[4] :
    #menor=tupla[0]
#elif tupla[1] < tupla[0] and tupla[1] < tupla[2] and tupla[1] < tupla[3] and tupla[1] < tupla[4] :
    #menor=tupla[1]
#elif tupla[2] < tupla[1] and tupla[2] < tupla[0] and tupla[2] < tupla[3] and tupla[2] < tupla[4] :
    #menor=tupla[2]
#elif tupla[3] < tupla[1] and tupla[3] < tupla[2] and tupla[3] < tupla[0] and tupla[3] < tupla[4] :
    #menor=tupla[3]
#elif tupla[4] < tupla[1] and tupla[4] < tupla[2] and tupla[4] < tupla[3] and tupla[4] < tupla[0] :
    #menor=tupla[4]
