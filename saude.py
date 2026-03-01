# este programa oferece ferramentas simples
# para calcular indicadores de saúde

# calcular IMC
def calcular_imc():
    print("\n===== CALCULADORA DE IMC =====")

    peso = float(input("Digite seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    # fórmula do IMC: peso dividido pela altura ao quadrado
    imc = peso / (altura ** 2)

    imc = round(imc, 2)
    print(f"\nSeu IMC é: {imc}")

    if imc < 18.5:
        print("Categoria: Abaixo do peso")
    elif imc < 25:
        print("Categoria: Peso normal ✓")
    elif imc < 30:
        print("Categoria: Sobrepeso")
    elif imc < 35:
        print("Categoria: Obesidade grau 1")
    elif imc < 40:
        print("Categoria: Obesidade grau 2")
    else:
        print("Categoria: Obesidade grau 3")


# 2 - calcular TMB
def calcular_tmb():
    print("\n===== TAXA METABÓLICA BASAL (TMB) =====")
    print("A TMB é a quantidade de calorias que seu corpo precisa por dia em repouso.\n")

    sexo = input("Digite seu sexo (M para masculino / F para feminino): ").upper()
    peso = float(input("Digite seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite sua altura em cm (ex: 175): "))
    idade = int(input("Digite sua idade: "))

    # fórmula de Harris-Benedict
    if sexo == "M":
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    elif sexo == "F":
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    else:
        print("Sexo inválido! Digite M ou F.")
        return  

    tmb = round(tmb, 2)
    print(f"\nSua TMB é: {tmb} calorias/dia")
    print("Isso significa que seu corpo precisa dessa quantidade de calorias só para funcionar em repouso.")



# 3 - hidratação
def calcular_hidratacao():
    print("\n===== CALCULADORA DE HIDRATAÇÃO =====")
    print("Descubra quantos litros de água você deve beber por dia.\n")

    peso = float(input("Digite seu peso em kg (ex: 70.5): "))

    # recomendação: 35ml de água por kg de peso corporal
    agua_ml = peso * 35
    agua_litros = round(agua_ml / 1000, 2)

    print(f"\nVocê deve beber aproximadamente {agua_litros} litros de água por dia.")
    print(f"Isso equivale a {round(agua_ml / 250)} copos de 250ml.")



# 4 - conversor de unidades
def converter_unidades():
    print("\n===== CONVERSOR DE UNIDADES DE SAÚDE =====")
    print("Escolha o que deseja converter:")
    print("1 - Peso: kg → libras")
    print("2 - Peso: libras → kg")
    print("3 - Altura: cm → polegadas")
    print("4 - Temperatura: °C → °F")
    print("5 - Temperatura: °F → °C")

    opcao = input("\nEscolha uma opção (1-5): ")

    if opcao == "1":
        kg = float(input("Digite o peso em kg: "))
        libras = round(kg * 2.205, 2)
        print(f"{kg} kg = {libras} libras")

    elif opcao == "2":
        libras = float(input("Digite o peso em libras: "))
        kg = round(libras / 2.205, 2)
        print(f"{libras} libras = {kg} kg")

    elif opcao == "3":
        cm = float(input("Digite a altura em cm: "))
        polegadas = round(cm / 2.54, 2)
        print(f"{cm} cm = {polegadas} polegadas")

    elif opcao == "4":
        celsius = float(input("Digite a temperatura em °C: "))
        fahrenheit = round((celsius * 9/5) + 32, 2)
        print(f"{celsius}°C = {fahrenheit}°F")

    elif opcao == "5":
        fahrenheit = float(input("Digite a temperatura em °F: "))
        celsius = round((fahrenheit - 32) * 5/9, 2)
        print(f"{fahrenheit}°F = {celsius}°C")

    else:
        print("Opção inválida!")



# menu 
def menu():
    print("\n" + "=" * 40)
    print("BEM-VINDO AOS UTILITÁRIOS DE SAÚDE")
    print("=" * 40)
    print("1 - Calcular IMC")
    print("2 - Calcular TMB (calorias diárias)")
    print("3 - Calcular hidratação diária")
    print("4 - Converter unidades de saúde")
    print("0 - Sair")
    print("=" * 40)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        calcular_imc()
    elif opcao == "2":
        calcular_tmb()
    elif opcao == "3":
        calcular_hidratacao()
    elif opcao == "4":
        converter_unidades()
    elif opcao == "0":
        print("\nAté logo! Cuide-se bem. 👋")
        return False  
    else:
        print("\nOpção inválida! Tente novamente.")

    return True  

# inicio do programa
if __name__ == "__main__":
    continuar = True
    while continuar:
        continuar = menu()