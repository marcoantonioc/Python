turma=[]
pessoa=[]
while True:
    nome=str(input("Indique o nome : "))
    nota1=float(input("Indique a 1º nota:"))
    nota2=float(input("Indique o 2º nota: "))

    pessoa.append(nome)
    pessoa.append(nota1)
    pessoa.append(nota2)

    turma.append(pessoa[:])
    pessoa.clear()

    continuar=str(input("Quer continuar [s]/[n]: ")).upper().strip()

    if continuar=="N":
        break
    elif continuar=="S":
        continue
    else:
        print("OPÇÃO INVÁLIDA")
        break
media=0
print("="*30)
print("Nº NOME  MEDIA")
for v in range(0,len(turma)):
    media=turma[v][1]+turma[v][2]
    print(v , turma[v][0], media)
    media=0
aluno=0
while True:
    aluno=int(input("Mostrar notas de que aluno [999 para sair]: "))
    if aluno == 999:
        break
    print(f"As notas do(a) {turma[aluno][0]} são {turma[aluno][1]} e {turma[aluno][2]}")
print("Adeus volte sempre! ")