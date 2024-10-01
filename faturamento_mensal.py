def calcular_percentuais(faturamento_por_estado):
    """Calcula o percentual de faturamento de cada estado em relação ao total."""
    total_faturamento = sum(faturamento_por_estado.values())

    percentuais = {}
    for estado, faturamento in faturamento_por_estado.items():
        percentuais[estado] = (faturamento / total_faturamento) * 100

    return percentuais


def main():
    # Dados de faturamento por estado
    faturamento_por_estado = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    # Calculando os percentuais
    percentuais = calcular_percentuais(faturamento_por_estado)

    # Exibindo os resultados
    print("Percentual de representação do faturamento por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")


# Executa o programa
main()