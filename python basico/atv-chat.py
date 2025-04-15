import os;

mensagens = [];

nome = input("Nome:");

while True:
    os.system("cls");

    if len(mensagens) > 0:
        for m in mensagens:
            print(m["nome"], "-", m["texto"])
    
    print("_____________________________________");

    texto = input("menssagem:");
    if texto == "exit":
        break;

    mensagens.append({"nome": nome, "texto": texto});





