#Faça um programa que leia uma lista de inteiros (o tamanho é informado pelo usuário) e verifique se ela é
# um palíndromo, ou seja, se ela é igual a si mesma quando lida de trás para frente. Exiba "É palíndromo"
# ou "Não é palíndromo". Exemplo: [1, 2, 3, 2, 1] → É palíndromo. [1, 2, 3, 4] → Não é palíndromo.

i = 0
lista = []

quantidade = int(input("Infrome o tamanho da sua lista(quantidade de elemntos): "))

while i < quantidade:
    num = int(input("Digite um numero inteiro:  "))
    lista.append(num)
    i += 1

copia = lista.copy()
copia.reverse()

if lista == copia:
    print(f'A lista {lista} é um palíndromo!')
else:
    print(f'A lista {lista} não é um palíndromo!')

