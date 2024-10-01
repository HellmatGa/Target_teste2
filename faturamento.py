import json

def carregar_faturamento(arquivo):
    """Carrega os dados de faturamento do arquivo JSON."""
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    return dados['faturamento_diario']

def calcular_faturamento(faturamento_diario):
    """Calcula o menor, maior e a quantidade de dias com faturamento acima da média."""
    faturamentos = list(faturamento_diario.values())

    # Ignorando dias sem faturamento (valores zero)
    faturamentos_validos = [f for f in faturamentos if f > 0]

    if not faturamentos_validos:
        return None, None, 0

    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)
    media_faturamento = sum(faturamentos_validos) / len(faturamentos_validos)

    # Contando dias com faturamento acima da média
    dias_acima_media = sum(1 for f in faturamentos_validos if f > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_media

def main():
    # Carregando os dados do faturamento
    faturamento_diario = carregar_faturamento('faturamento.json')

    # Calculando os resultados
    menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

    # Exibindo os resultados
    print(f'Menor faturamento: R$ {menor:.2f}')
    print(f'Maior faturamento: R$ {maior:.2f}')
    print(f'Dias com faturamento acima da média: {dias_acima_media}')

# Executa o programa
main()