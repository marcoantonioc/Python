lista=[]
total=0
total1=0
expressao=str(input("Indique uma expressao: "))

#for v in expressao:
    #if v =="(":
        #total+=1
    #if v ==")":
        #total1+=1
#if total==total1:
    #print("A expressão está CERTA ")
#elif total!=total1:
    #print("A expressao está ERRADA")
#else:
    #print("ALGUMA COISA ESTÁ ERRADA")


#OU

for v in expressao:
    if v=="(":
        lista.append("(")
    elif v==")":
        if len(lista)>0:
            lista.pop()
        else:
            break
if len(lista)>0:
    print("A expressao está errada !")
else:
    print("A expressao está certa !")