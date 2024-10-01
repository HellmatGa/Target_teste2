def inverter_string(s):
    """Inverte os caracteres de uma string."""
    string_invertida = ''
    # Itera pelos caracteres da string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida


def main():
    # Entrada do usuário ou string pré-definida
    string_original = input(
        "Informe uma string para inverter (ou pressione Enter para usar a pré-definida): ") or "Exemplo de string"

    # Invertendo a string
    string_invertida = inverter_string(string_original)

    # Exibindo o resultado
    print(f"String original: {string_original}")
    print(f"String invertida: {string_invertida}")


# Executa o programa
main()