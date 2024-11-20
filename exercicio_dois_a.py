print('CADASTRO DE PRODUTOS')
print('********************')


def cadastrar():
    estoque = [
        {f'Produto: {nome_produto1}, Quantidade: {valor_1}'}, 
        {f'Produto: {nome_produto2}, Quantidade: {valor_2}'},
        {f'Produto: {nome_produto3}, Quantidade: {valor_3}'}
               ]
    
    
    return estoque


nome_produto1 = str(input('Digite o nome de um produto: ').lower())
valor_1 = int(input('Digite a quantidade desse produto: '))

nome_produto2 = str(input('Digite o nome de um segundo produto: ').lower())
valor_2 = int(input('Digite a quantidade desse segundo produto: '))

nome_produto3 = str(input('Digite o nome de um terceiro produto: ').lower())
valor_3 = int(input('Digite a quantidade desse terceiro produto: '))

resultado = cadastrar()

print(resultado)

