palavras=("APRENDER",'PROGRAMAR','LINNGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR',
          'TRABALHO','MERCADO','FUTURO',"CDFG")

for termos in palavras:
    print(f"Nas palavra {termos},temos ")
    for letras in termos:
        if letras in "AEIOU":
            print(letras)
