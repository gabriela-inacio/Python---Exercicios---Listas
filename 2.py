#Faça um programa que leia números inteiros do usuário até que ele digite 0 (o zero não deve entrar na
# lista). Após a leitura, gere duas novas listas: uma contendo apenas os números pares e outra contendo
#apenas os ímpares. Exiba as duas listas e a quantidade de elementos em cada uma

i = 0
pares = []
impares = []

while True:

    numeros = int(input("Digite um numero inteiro.\nDigite 0 para encerrar! "))
    
    if numeros == 0:
       break
    
    if numeros % 2 == 0:
        pares.append(numeros)
    elif numeros % 2 != 0:
        impares.append(numeros)

print(f'Numero pares: {pares}' )
print(f'Numeros impares: {impares}')
print(f'A quantidade de numeros pares é de: {len(pares)} e de impares é de: {len(impares)}')