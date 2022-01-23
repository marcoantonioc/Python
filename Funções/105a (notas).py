def notas(*num,sit=False):
    """
    ola puta

    """
    resumo=dict()
    resumo['Total']=len(num)
    resumo['Maior']=max(num)
    resumo['Menor']=min(num)
    resumo['Media']=sum(num)/len(num)
    if sit:
        if resumo['Media']>=7:
            resumo['Situação']='Boa'
        elif resumo['Media']>=5:
            resumo['Situação']='Razoavel'
        else:
            resumo['Situação']='Ma'
    return resumo
resp=notas(5.5,2.5,9,8.5,sit=True)
print(resp)
