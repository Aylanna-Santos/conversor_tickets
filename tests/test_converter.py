import pytest
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