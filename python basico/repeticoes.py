notas = [];

for i in range(3):
    aluno = input("Digite o código do aluno:" );
    nota = float(input("Digite a nota do aluno: "));
    resultado = [aluno, nota];
    notas.append(resultado);

for i in notas:
    aluno = i[0];
    nota = i[1];
    print("Aluno:", aluno, "Nota:", nota);

i = 0
while i < len(notas):
    aluno = notas[i][0]
    nota = notas[i][1]
    print("Aluno:", aluno, "Nota:", nota)
    i += 1

