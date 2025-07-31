lista_1 = [1,2,4]

dobro = list(map(lambda x: x*2, lista_1))
print(dobro) 

lista_2 = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 32},
    {"nome": "Carla", "idade": 28},
]

so_nome = list(map(lambda p: p['nome'], lista_2))
so_idade = list(map(lambda p: p['idade'], lista_2))
tudo = list(map(lambda p: f'{p['nome']} tem {p['idade']} anos', lista_2))

print(so_nome)
print(so_idade)
print(tudo)