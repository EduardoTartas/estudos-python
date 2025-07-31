from first_class import dobro, quadrado

def processar(titulo, lista, funcao):
    if callable(funcao):
        print(f'Processando:{titulo}')
        for i in lista:
            print(i, '=>', funcao(i))


processar('Dobros de um a dez', range(1,11), dobro)

processar('Quadrado de um a dez', range(1,11), quadrado)