def avaliar_cliente(cliente) -> str:
    """
    Avalia um cliente com base em regras fixas e retorna 'Aprovado' ou 'Negado'.
    """

    # Regra 1: Valor alto e sem poupança
    if cliente['Credit amount'] > 5000 and cliente['Saving accounts'] in ['unknown', 'little']:
        return 'Negado'

    # Regra 2: Jovem com prazo longo
    if cliente['Age'] < 25 and cliente['Duration'] > 24 :
        return 'Negado'
    
    # Regra 2: Pouco saldo e longo prazo
    if cliente['Credit amount'] in ['little','unknown'] and ['Duration'] > 36:
        return 'Negado'
    
    return 'Aprovado'
