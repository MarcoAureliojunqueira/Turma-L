# exercicio 4
def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial


resultado = calcular_fatorial(5)
print(resultado)  # Saída: 120