# Plano de Teste - Conversor de Tickets

## Objetivo
Validar o funcionamento da aplicação de conversão de valores monetários em tickets, garantindo que:
- Cada ticket vale R$ 5,00.
- O sistema calcula corretamente a quantidade de tickets.
- O sistema informa o troco ou erro quando necessário.

---

## Testes de Caixa Preta
Testes baseados em entradas e saídas esperadas, sem considerar a lógica interna.

| Caso de Teste | Entrada | Saída Esperada | Resultado Esperado |
|---------------|---------|----------------|--------------------|
| Valor exato   | 20      | 4 tickets, troco 0 | Sucesso |
| Valor com troco | 22    | 4 tickets, troco 2 | Sucesso |
| Valor insuficiente | 3 | 0 tickets, troco 3 | Sucesso |
| Valor zero    | 0       | 0 tickets, troco 0 | Sucesso |
| Valor múltiplo | 50     | 10 tickets, troco 0 | Sucesso |

---

## Testes de Caixa Branca
Testes baseados na lógica interna e fluxos de execução do código.

| Caso de Teste | Cenário Interno | Resultado Esperado |
|---------------|-----------------|--------------------|
| Fluxo normal  | Entrada múltipla de 5 | Tickets calculados corretamente |
| Fluxo com resto | Entrada não múltipla de 5 | Troco retornado corretamente |
| Fluxo de erro | Entrada negativa | Levantar `ValueError` |
| Fluxo limite  | Entrada igual a 0 | Retornar 0 tickets e 0 troco |
| Fluxo máximo  | Entrada grande (ex: 1000) | Calcular tickets sem falha |

---

## Conclusão
- Os testes de **caixa preta** garantem que as entradas e saídas estão corretas.  
- Os testes de **caixa branca** asseguram que todos os caminhos internos do código são cobertos.  
- O sistema atende aos requisitos da atividade AV2 e está pronto para integração com GitHub Actions.
