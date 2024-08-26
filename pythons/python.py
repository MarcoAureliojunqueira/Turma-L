# exercio 1
valor1 = int(input("Digite o Primeiro numero: "))
valor2 = int(input("Digite o Segundo numero: "))

print("resultado do  exercicio 1 = ", valor1 + valor2)
print()
# exercio 2
nome = (input("Digite o seu nome: "),)
email = (input("Digite o seu email: "),)
produto = (input("Digite o seu Produto:"),)
codigo = (int(input("Digite o codigo do seu produto:")),)
preço = (int(input("Digite o preço do seu produto:")),)

print(
    "seu nome :",
    nome,
    "seu email :",
    email,
    "seu produto :",
    produto,
    "seu codigo :",
    codigo,
    "seu preço:",
    preço,
)
print()
# Programa para converter centímetros em metros
centimetros = float(input("Digite o valor em centímetros: "))
metros = centimetros / 100
print(f"{centimetros} centímetros é igual a {metros} metros.")

print()
# Programa para calcular a área de um quadrado/retângulo
largura = float(input("Digite a largura (em metros): "))
altura = float(input("Digite a altura (em metros): "))
area = largura * altura
print(f"A área do quadrado/retângulo é: {area} metros quadrados.")
