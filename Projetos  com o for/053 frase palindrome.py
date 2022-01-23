frase=str(input('Indique uma frase (sem pontoacao): ')).strip().upper().replace(' ', '')


frase2=frase.split()

for letra in range(len(frase) -1,-1,-1):
    print(frase[letra] ,end=' ')

if frase != frase[letra]:
    print('\n E um Palindromo')
elif frase==frase[letra]:
    print('\n Nao e um palindromo')









