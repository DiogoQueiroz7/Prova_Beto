print('TABELA VERDADE')
print('**************')

print('P\tQ\tnotP\tnotPandQ')

valores = [True, False]

for P in valores:
    for Q in valores:
        not_p = not P
        not_p_and_q = not P and  Q
        print(f'{P}\t{Q}\t{not_p}\t{not_p_and_q}')
        