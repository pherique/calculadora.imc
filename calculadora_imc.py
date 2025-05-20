# Calculadora de IMC simples em Python

# Solicita ao usuário que insira o peso em kg
peso = float(input("Digite seu peso (em kg): "))  # exemplo: 70

# Solicita ao usuário que insira a altura em metros
altura = float(input("Digite sua altura (em metros): "))  # exemplo: 1.75

# Calcula o IMC usando a fórmula
imc = peso / (altura ** 2)  # altura ** 2 = altura ao quadrado

# Exibe o valor do IMC com duas casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

# Verifica em qual faixa de classificação o IMC se encaixa
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Classificação: Obesidade grau 1")
elif 35 <= imc < 39.9:
    print("Classificação: Obesidade grau 2")
else:
    print("Classificação: Obesidade grau 3 (obesidade mórbida)")
