def calcular_preco(produto, condicao_pagamento, parcelas):
    """Calcula o valor a ser pago com base no preço do produto, condição de pagamento e número de parcelas."""
    
    if condicao_pagamento == 'avista':
        if parcelas == 1:
   
            preco = produto * 0.90
        elif parcelas == 2:

            preco = produto * 0.95
        else:
            return "Número de parcelas inválido para pagamento à vista."
    elif condicao_pagamento == 'parcelado':
        if parcelas == 1:
            return "Pagamento parcelado não é permitido em uma única parcela."
        elif parcelas == 2:
    
            preco = produto
        elif parcelas >= 3:
   
            preco = produto * 1.20
        else:
            return "Número de parcelas inválido para pagamento parcelado."
    else:
        return "Condição de pagamento inválida."
    
    return preco

def main():
    """Função principal para executar o cálculo de pagamento do produto."""
    print("Cálculo de valor a ser pago por produto")
    
    try:
        produto = float(input("Digite o preço do produto: R$ "))
    except ValueError:
        print("Preço inválido. Por favor, insira um número.")
        return

    condicao_pagamento = input("Condição de pagamento (avista/parcelado): ").strip().lower()
    
    if condicao_pagamento == 'avista':
        try:
            parcelas = int(input("Número de parcelas (1 para dinheiro/cheque, 2 para cartão): "))
        except ValueError:
            print("Número de parcelas inválido. Deve ser um número inteiro.")
            return
    elif condicao_pagamento == 'parcelado':
        try:
            parcelas = int(input("Número de parcelas (2 ou mais): "))
        except ValueError:
            print("Número de parcelas inválido. Deve ser um número inteiro.")
            return
    else:
        print("Condição de pagamento inválida. Deve ser 'avista' ou 'parcelado'.")
        return

    preco = calcular_preco(produto, condicao_pagamento, parcelas)
    
    if isinstance(preco, str):
        print(preco)
    else:
        print(f"O valor a ser pago é: R$ {preco:.2f}")

if __name__ == "__main__":
    main()
