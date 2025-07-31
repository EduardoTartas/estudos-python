from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt-BR')

meses = list(zip(month_name, mdays))
meses_31 = list(filter(lambda m: m[1] == 31, meses))
teste = list(map(lambda m: f'{m[0]} - {m[1]}', meses_31))

for i in teste:
    print(i)

print('----------')
#forma mais facil sem usar map reduce ou filter
aaa = [f'{nome} - {dias}' for nome, dias in meses if dias == 31]

for i in aaa:
    print(i)