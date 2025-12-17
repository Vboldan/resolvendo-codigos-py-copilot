# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
# # Solicitando números (usamos float para permitir decimais)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a operação (+, -, *, /): ")
if operation == "+":
    soma = num1 + num2
    print(f"A soma entre {num1} e {num2} é: {soma}")
elif operation == "-":
    subtracao = num1 - num2
    print(f"A subtração entre {num1} e {num2} é: {subtracao}")
elif operation == "*":
    multiplicacao = num1 * num2
    print(f"A multiplicação entre {num1} e {num2} é: {multiplicacao}")
elif operation == "/":
    if num2 != 0:
        divisao = num1 / num2
        print(f"A divisão entre {num1} e {num2} é: {divisao}")
    else:
        print("Erro: Divisão por zero não é permitida.")

soma = num1 + num2

#print(f"A soma entre {num1} e {num2} é: {soma}")
