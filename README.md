# Conversor de Tickets

## Descrição
Aplicação acadêmica que simula um sistema de conversão de valores monetários em tickets para parques de diversão ou máquinas.  
Cada ticket vale R$ 5,00. O sistema calcula a quantidade de tickets, informa se há troco ou se o valor é insuficiente.

---

## Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Aylanna-Santos/conversor_tickets.git
   cd conversor_tickets
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   source venv/Scripts/activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o programa principal:
   ```bash
   python src/main.py
   ```

---

## Como rodar os testes

1. Certifique-se de estar no ambiente virtual.  
2. Execute os testes com PyTest:
   ```bash
   pytest -v
   ```
3. Para gerar relatório em XML:
   ```bash
   pytest --junitxml=tests/test-report.xml
   ```
   
---

## Integração com DevOps
Este projeto possui pipeline configurado em GitHub Actions (.github/workflows/ci.yml) que:
- Faz checkout do código.  
- Configura ambiente Python.  
- Instala dependências.  
- Executa testes com PyTest.  
- Gera relatório em XML para consulta.  

---

## Conclusão
O projeto atende aos requisitos do Projeto AV2:
- Plano de teste (caixa preta e branca).  
- Código de teste automatizado.  
- Relatório de execução.  
- Equipe com matrículas.  
- Pipeline DevOps integrado no GitHub Actions.
