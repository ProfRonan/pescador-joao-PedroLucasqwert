"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    K=float(input("Quatos quilos foram pescados?\n"))
    M=(K-50)*4
    if M < 0:
       M = 0
    print(f"O peixe pescado tem {K}kg, a multa devida é R$ {M:.2f}.")   


if __name__ == '__main__':
    main()
