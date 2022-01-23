escola={}

escola['nome']=str(input("Indique o seu nome :"))
escola['media']=float(input(f"Indique a media a sua media {escola['nome']}:"))

print("="*30)
print(f"Nome:{escola['nome']}")
print(f"A media é : {escola['media']}")

if escola['media']>=7:
    print("Situação é igual a APROVADO")
elif escola['media']<7:
    print("A situação é igual a REPROVADO")