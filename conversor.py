# Conversor de Tickets
# Define o valor fixo de cada ticket e a função de conversão

TICKET_VALUE = 5  # cada ticket vale R$ 5,00

def calcular_tickets(valor):
    """
    Converte um valor em reais para quantidade de tickets e calcula o troco.
    :param valor: valor em reais (int ou float)
    :return: (tickets, troco)
    """
    if valor < 0:
        raise ValueError("Valor inválido. O valor deve ser positivo.")
    
    tickets = valor // TICKET_VALUE
    troco = valor % TICKET_VALUE
    return tickets, troco