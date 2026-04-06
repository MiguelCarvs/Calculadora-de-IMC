# Definition of functions and classifications
def calc_imc(peso, altura):
    return peso / (altura ** 2)

def classific_imc(imc):
    if imc < 18.5:
        return "Você está abaixo do peso."
    elif imc < 24.9:
        return "Você está em um peso ideal."
    elif imc < 29.9:
        return "Você está em sobrepeso."
    elif imc < 34.9:
        return "Obesidade grau I"
    elif imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

# Start of the aplication
def main():
    print("=== Calculadora de Índice de Massa Corporal ===")

    try:
        peso = float(input("Digite seu peso(Kg): ").strip().replace(",", "."))
        altura = float(input("Digite sua altura(M): ").strip().replace(",", "."))

        if peso <= 0 or altura <= 0:
            print("Altura e peso devem ser maiores que zero.")
            return

        imc = calc_imc(peso, altura)
        classificacao = classific_imc(imc)

        print("\n--- Resultado ---")
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")

    except ValueError:
        print("Digite números válidos.")

if __name__ == "__main__":
    main()

input("\nPrecione tecla enter para sair: ")
