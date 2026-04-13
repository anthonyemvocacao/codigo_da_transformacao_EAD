 #1. Função de saudação personalizada
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")


# 2. Função para calcular média e verificar aprovação
def calcular_media(notas):
    media = sum(notas) / len(notas)
    print(f"Média: {media:.2f}")
    
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")


# 3. Função para retornar o maior e o menor número da lista
def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor


# Desafio Extra: Sistema simples de login
def validar_login(usuarios, usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    return False


# ============================
# Testando as funções
# ============================

# 1
saudacao("Maria")

# 2
notas_aluno = [8.0, 7.5, 6.0]
calcular_media(notas_aluno)

# 3
numeros = [10, 5, 30, 2, 8]
maior, menor = maior_menor(numeros)
print(f"Maior: {maior}, Menor: {menor}")

# Desafio Extra
usuarios_db = {
    "admin": "1234",
    "user": "abcd"
}

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if validar_login(usuarios_db, usuario, senha):
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos.")
