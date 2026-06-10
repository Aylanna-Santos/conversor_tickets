from conversor import calcular_tickets

def main():
    print("=== Conversor de Tickets ===")
    try:
        valor = int(input("Digite o valor em reais: "))
        tickets, troco = calcular_tickets(valor)

        if tickets > 0 and troco > 0:
            print(f"Você inseriu R$ {valor}. Foram gerados {tickets} tickets e R$ {troco} de troco.")
        elif tickets > 0 and troco == 0:
            print(f"Você inseriu R$ {valor}. Foram gerados {tickets} tickets sem troco.")
        else:
            print(f"Você inseriu R$ {valor}. Não foi possível gerar tickets. O valor será retornado.")
            
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()