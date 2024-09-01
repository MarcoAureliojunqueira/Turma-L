# Com base nos conhecimentos adquiridos ao longo desta aula, resolva a lista de
# exercícios sobre estrutura de repetição
# Você pode usar o FOR ou WHILE para resolver os exercícios.

# 1) Faça um programa que mostre a mensagem "hello world" cinco vezes.
x = 0
while x < 5:
    x += 1
    print("hello world")


# 1) Faça um programa que mostre todos os números de 1 até 150.
d = 1
while d < 150:
    d += 1
    print(d)

# 1) Faça um programa que mostre uma contagem regressiva que
# inicia em 10 e termina em 0.
p = 10
while p > 0:
    p -= 1
    print(p)

# 1) Faça um programa que mostre todos os números pares de 1 até 200.

for r in range(1, 200):
    if (r % 2 == 0):
        print(r)
# 1) Faça um programa que gere as tabuadas do 1 até o 10.
# Função para gerar a tabuada de um número

# 1) Faça um programa em que o usuário digita um número inteiro e o programa
# exibe todos os números ímpares do 1 até o valor inserido.
digito = int(input("Digite o um numero inteiro:"))

print("Números ímpares de 1 até", digito, ":")
for i in range(1, digito + 1):
    if i % 2 != 0:
        print(i)
