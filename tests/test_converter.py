import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from conversor import calcular_tickets

def test_valor_exato():
    tickets, troco = calcular_tickets(20)
    assert tickets == 4
    assert troco == 0

def test_valor_com_troco():
    tickets, troco = calcular_tickets(22)
    assert tickets == 4
    assert troco == 2

def test_valor_insuficiente():
    tickets, troco = calcular_tickets(3)
    assert tickets == 0
    assert troco == 3

def test_valor_negativo():
    with pytest.raises(ValueError):
        calcular_tickets(-5)

# Testes parametrizados para vários cenários
@pytest.mark.parametrize("valor,esperado_tickets,esperado_troco", [
    (0, 0, 0),   # valor zero
    (5, 1, 0),   # valor exato de um ticket
    (7, 1, 2),   # valor com troco
    (50, 10, 0), # múltiplos de tickets
])
def test_varios_valores(valor, esperado_tickets, esperado_troco):
    tickets, troco = calcular_tickets(valor)
    assert tickets == esperado_tickets
    assert troco == esperado_troco
