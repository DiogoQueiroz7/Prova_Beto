print('TABELA VERDADE')
print('**************')

print('P\tQ\tR\tP^Q\t(P^Q)vR')

valores = [True, False] 
#(p^q)Vr
for P in valores:
    for Q in valores:
        for R in valores:
            p_and_q = P and Q
            p_and_q_or_r = (p_and_q) or R
            
            print(f'{P}\t{Q}\t{R}\t{p_and_q}\t{p_and_q_or_r}')
            


