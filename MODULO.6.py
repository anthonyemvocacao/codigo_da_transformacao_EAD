
### 1. Operações matemáticas (corrigido)**


# Programa que realiza operações básicas

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Evita erro de divisão por zero
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Não é possível dividir por zero"

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)


### 2. Maior entre dois números 


# Programa que mostra qual número é maior

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os dois números são iguais")



### 3. Classificação por idade (ok)**



idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")


### 4. Menu com while


# Menu interativo

while True:
    print("\n--- MENU ---")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado:", n1 + n2)

    elif opcao == "2":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado:", n1 - n2)

    elif opcao == "3":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")
