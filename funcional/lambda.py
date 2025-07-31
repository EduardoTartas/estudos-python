a1 = [1,2,3]

a2 = list(map(lambda i: i*2, a1))
print(a2)

compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14}
)

totais = tuple(map(lambda compra: compra['quantidade'] * compra['preco'],compras))

print(totais)
print(sum(totais))

