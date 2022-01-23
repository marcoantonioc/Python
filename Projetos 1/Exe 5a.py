A=80000
Apercentagem=(A/100)*3

B=200000
Bpercentagem=(B/100)*1.5

anos=0
while B>=A:
    anos += 1
    A+=Apercentagem
    B+=Bpercentagem

print(anos)

