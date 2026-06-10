# Relatório de Execução dos Testes - Conversor de Tickets

## Objetivo
Registrar os resultados da execução dos testes automatizados com PyTest, validando o funcionamento do sistema de conversão de tickets.

---

## Ambiente de Teste
- Sistema Operacional: Windows 11
- Python: 3.14.0
- Framework de Teste: PyTest 9.0.3
- Ambiente Virtual: venv

---

## Execução dos Testes
Comando utilizado:
```bash
pytest -v
==== test session starts ====
platform win32 -- Python 3.14.0, pytest-9.0.3
collected 5 items

tests/testconversor.py::testvalor_exato PASSED
tests/testconversor.py::testvalorcomtroco PASSED
tests/testconversor.py::testvalor_insuficiente PASSED
tests/testconversor.py::testvalor_negativo PASSED
tests/testconversor.py::testvarios_valores PASSED

==== 5 passed in 0.05s ====
```

---

## Conclusão
- Todos os testes passaram com sucesso.  
- O sistema atende aos requisitos de caixa preta e caixa branca.  
- O projeto está pronto para entrega e integração com GitHub Actions.

---

## Equipe
- Aylanna Santos de França– Matrícula 01710642  
- Pedro Gutemberg de Lima Silva – Matrícula 01698431
