def sum (valor1, valor2):
    return valor1 + valor2;

while True:
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    print(v1, "+", v2, "=", sum(v1, v2))
    status = input("Deseja continuar? (s/n): ")
    if status.lower() == "n":
        break
    