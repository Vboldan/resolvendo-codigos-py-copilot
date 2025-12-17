palavra = input("Digite uma palavra para verificar se é um palíndromo: ").lower()

# Invertendo a string usando fatiamento (slicing) [início:fim:passo]
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
    print(f"O inverso seria: {palavra_invertida}")
