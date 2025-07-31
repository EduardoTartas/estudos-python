def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular

dobro = multiplicar(3)
print(dobro)
print(dobro(3))