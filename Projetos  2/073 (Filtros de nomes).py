tabela=('Athletico-PR','Atlético-GO','Atlético-MG','Bahia','Botafogo',
        'Botafogo','Bragantino','Ceará','Corinthians','Coritiba',
        'Flamengo','Fluminense','Fortaleza','Chapecoense','Goiás','Grêmio',
        'Internacional','Palmeiras','Santos','São Paulo','	Sport','Vasco')

print(f'Os primeiros colocados foram os : {tabela[0:5]}')
print()
print(f'Os últimos 4 colocados foram {tabela[-4:]} ')
print()
print(f'A lista de ordem Alfabética : {sorted(tabela)}')
print()
print(f'E o Chapecoense está na posição {tabela.index("Chapecoense")+1}')

