print('Tabela Verdade')
print('**************')

#not r or not q

print('R\tQ\tnotR\tnotQ\tnotRornotQ')

valores = [True, False]

for R in valores:
    for Q in valores:
        not_r = not R
        not_q = not Q
        not_r_or_not_q = not R or not Q
        print(f'{R}\t{Q}\t{not_r}\t{not_q}\t{not_r_or_not_q}')