'''
arquivo = open('./pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('nome: {} | idade: {}'.format(*registro.split(',')))
'''

'''
arquivo = open('./pessoas.csv')
for registro in arquivo:
    print('nome: {} | idade: {}'.format(*registro.split(',')), end='')
arquivo.close()
'''

'''
with open('./pessoas.csv') as pessoas:
    with open('./pessoas.txt', 'w') as file:
        for registro in pessoas:
            registro = registro.strip().split(',')
            print('Nome: {} | Idade: {}'.format(*registro), file=file)
'''

import csv
with open('./pessoas.csv') as pessoas:
      for registro in csv.reader(pessoas):
            print('Nome: {} | Idade: {}'.format(*registro))
            

