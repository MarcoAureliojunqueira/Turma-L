# exercicio 1
def soma_numeros(a, b):
    return a + b


resultado = soma_numeros(3, 7)
print(resultado)  # Saída: 10


# exercicio 2
def eh_par(numero):
    if numero % 2 == 0:
        print(True)
    else:
        print(False)


print(eh_par(4))  # Saída: True
print(eh_par(5))  # Saída: False


# exercicio 3
def reverter_string(texto):
    return texto[::-1]


resultados = reverter_string("nohtyP")
print(resultados)  # Saída: "Python"


# exercicio 4
def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial


resultado = calcular_fatorial(5)
print(resultado)  # Saída: 120
