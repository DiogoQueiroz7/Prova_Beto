print('ANÁISE DE VENDA')
print('***************')

produto1 = str(input('Digite o nome do seu primeiro produto: ').lower())
qtd1 = int(input('Digite o número do quanto você vendeu esse produto: '))
preco1 = float(input('Digite o preco desse produto: '))

produto2 = str(input('Digite o nome do seu segundo produto: ').lower())
qtd2 = int(input('Digite o número do quanto você vendeu esse produto: '))
preco2 = float(input('Digite o preco desse produto: '))

produto3 = str(input('Digite o nome do seu terceiro produto: ').lower())
qtd3 = int(input('Digite o número do quanto você vendeu esse produto: '))
preco3 = float(input('Digite o preco desse produto: '))

produto4 = str(input('Digite o nome do seu quarto produto: ').lower())
qtd4 = int(input('Digite o número do quanto você vendeu esse produto: '))
preco4 = float(input('Digite o preco desse produto: '))

produto5 = str(input('Digite o nome do seu quinto produto: ').lower())
qtd5 = int(input('Digite o número do quanto você vendeu esse produto: '))
preco5 = float(input('Digite o preco desse produto: '))

produto6 = str(input('Digite o nome do seu sexto produto: ').lower())
qtd6 = int(input('Digite o número do quanto você vendeu esse produto: '))
preco6 = float(input('Digite o preco desse produto: '))

produto7 = str(input('Digite o nome do seu sétimo produto: ').lower())
qtd7 = int(input('Digite o número do quanto você vendeu esse produto: '))
preco7 = float(input('Digite o preco desse produto: '))

produto8 = str(input('Digite o nome do seu oitavo produto: ').lower())
qtd8 = int(input('Digite o número do quanto você vendeu esse produto: '))
preco8 = float(input('Digite o preco desse produto: '))

produto9 = str(input('Digite o nome do seu nono produto: ').lower())
qtd9 = int(input('Digite o número do quanto você vendeu esse produto: '))
preco9 = float(input('Digite o preco desse produto: '))

produto10 = str(input('Digite o nome do seu décimo produto: ').lower())
qtd10 = int(input('Digite o número do quanto você vendeu esse produto: '))
preco10 = float(input('Digite o preco desse produto: '))

vendas = [
    {f'produto: {produto1}, quantidade: {qtd1}, preco_unitario: {preco1}'},
    {f'produto: {produto2}, quantidade: {qtd2}, preco_unitario: {preco2}'},
    {f'produto: {produto3}, quantidade: {qtd3}, preco_unitario: {preco3}'},
    {f'produto: {produto4}, quantidade: {qtd4}, preco_unitario: {preco4}'},
    {f'produto: {produto5}, quantidade: {qtd5}, preco_unitario: {preco5}'},
    {f'produto: {produto6}, quantidade: {qtd6}, preco_unitario: {preco6}'},
    {f'produto: {produto7}, quantidade: {qtd7}, preco_unitario: {preco7}'},
    {f'produto: {produto8}, quantidade: {qtd8}, preco_unitario: {preco8}'},
    {f'produto: {produto9}, quantidade: {qtd9}, preco_unitario: {preco9}'},
    {f'produto: {produto10}, quantidade: {qtd10}, preco_unitario: {preco10}'}
]

print(vendas)
