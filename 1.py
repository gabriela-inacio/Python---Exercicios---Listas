#Faça um programa que leia 7 números inteiros do usuário, armazene-os em uma lista e, ao final, exiba: 
# a soma, a média, o maior e o menor número da lista.

i = 0
soma = 0
lista = []

while i < 7:
    numeros = int(input("Digite um numero inteiro: "))
    lista.append(numeros)
    i += 1
    soma += numeros

media = soma / 7
maior = max(lista)
menor = min(lista)

print(lista)
print(f'A soma dos numeros {lista} é: {soma}')
print(f'A média dos números {lista} é: {media}')
print(f'O maior numero da lista {lista} é: {maior}')
print(f'O menor numero da lsita {lista} é: {menor}')


