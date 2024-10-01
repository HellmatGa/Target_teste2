def calcular_fibonacci(n):
    """Calcula a sequência de Fibonacci até o enésimo termo."""
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)
    return fibonacci


def pertence_a_fibonacci(numero):
    """Verifica se um número pertence à sequência de Fibonacci."""
    # Para verificar, calculamos a sequência de Fibonacci até um limite razoável.
    fibonacci = calcular_fibonacci(30)  # Calcula os primeiros 30 termos
    return numero in fibonacci


def main():
    # Entrada do usuário
    numero = int(input("Informe um número: "))

    # Verifica se o número pertence à sequência de Fibonacci
    if pertence_a_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")


# Executa o programa
main()