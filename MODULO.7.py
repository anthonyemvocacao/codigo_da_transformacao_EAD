

## 1. Lista de compras (adicionar/remover/visualizar)

# Lista de compras

lista = []

while True:
    print("\n1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        item = input("Digite o item: ")
        lista.append(item)
        print("Item adicionado!")

    elif opcao == "2":
        item = input("Digite o item para remover: ")
        if item in lista:
            lista.remove(item)
            print("Item removido!")
        else:
            print("Item não encontrado!")

    elif opcao == "3":
        print("Lista de compras:", lista)

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")


## 2. Dicionário de aluno

# Dados de um aluno

aluno = {
    "nome": input("Nome: "),
    "idade": int(input("Idade: ")),
    "nota1": float(input("Nota 1: ")),
    "nota2": float(input("Nota 2: "))
}

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(chave, ":", valor)
 

## 3. Pares e ímpares

# Separar pares e ímpares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Pares:", pares)
print("Ímpares:", impares)




## Desafio Extra (Agenda de contatos)

# Agenda de contatos

agenda = {}

while True:
    print("\n1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Remover contato")
    print("4 - Ver agenda")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
        print("Contato salvo!")

    elif opcao == "2":
        nome = input("Nome para buscar: ")
        if nome in agenda:
            print("Telefone:", agenda[nome])
        else:
            print("Contato não encontrado!")

    elif opcao == "3":
        nome = input("Nome para remover: ")
        if nome in agenda:
            del agenda[nome]
            print("Removido!")
        else:
            print("Contato não encontrado!")

    elif opcao == "4":
        print("Agenda:", agenda)

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")


