"""
Calculadora Simples
--------------------
"""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def obter_numero(mensagem):
    """Solicita um número ao usuário, repetindo até que seja válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.\n")


def exibir_menu():
    print("=" * 30)
    print("        CALCULADORA")
    print("=" * 30)
    print("1 - Soma (+)")
    print("2 - Subtracao (-)")
    print("3 - Multiplicacao (*)")
    print("4 - Divisao (/)")
    print("5 - Sair")
    print("=" * 30)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "5":
            print("Encerrando a calculadora. Até logo!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida! Tente novamente.\n")
            continue

        a = obter_numero("Digite o primeiro número: ")
        b = obter_numero("Digite o segundo número: ")

        try:
            if opcao == "1":
                resultado = somar(a, b)
                simbolo = "+"
            elif opcao == "2":
                resultado = subtrair(a, b)
                simbolo = "-"
            elif opcao == "3":
                resultado = multiplicar(a, b)
                simbolo = "*"
            elif opcao == "4":
                resultado = dividir(a, b)
                simbolo = "/"

            print(f"\nResultado: {a} {simbolo} {b} = {resultado}\n")

        except ZeroDivisionError as erro:
            print(f"\nErro: {erro}\n")


if __name__ == "__main__":
    main()
