from functools import reduce


pessoas = [
    {"nome": "Ana", "idade": 8},      
    {"nome": "Bruno", "idade": 16},   
    {"nome": "Carla", "idade": 22},
    {"nome": "Daniel", "idade": 45},  
    {"nome": "Eduarda", "idade": 67}, 
    {"nome": "Felipe", "idade": 72},  
    {"nome": "Gabriela", "idade": 5}, 
    {"nome": "Henrique", "idade": 34},
    {"nome": "Isabela", "idade": 13}, 
    {"nome": "João", "idade": 80}     
]

menores = list(filter(lambda p: p['idade']<18, pessoas))

soma_idade = reduce(lambda idade, p: idade + p['idade'], menores, 0)


print(soma_idade)
