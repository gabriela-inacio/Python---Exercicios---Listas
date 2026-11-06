#Dadas duas listas já em ordem crescente, produza uma terceira lista contendo todos os elementos das
#duas, também em ordem crescente. O tamanho de cada lista e seus elementos são informados pelo
#usuário (suponha que ele digite os elementos já ordenados). Não é permitido usar sort() nem sorted() na
#lista final — você deve aproveitar que as listas originais já estão ordenadas para fazer a mesclagem.
#Exemplo: [1, 4, 6, 9] e [2, 3, 5, 10, 11] → [1, 2, 3, 4, 5, 6, 9, 10, 11].

lista1 = []
lista2 = []
lista_final = []

i = 0
tam1 = int(input("Informe o tamanho da primeira lista: "))

while i < tam1:
    num1 = int(input("Digite um número: "))
    lista1.append(num1)
    i += 1

j = 0
tam2 = int(input("Informe o tamanho da segunda lista: "))

while j < tam2:
    num2 = int(input("Digite um número: "))
    lista2.append(num2)
    j += 1

i = 0
j = 0

while i < len(lista1) and j < len(lista2):
    if lista1[i] < lista2[j]:
        lista_final.append(lista1[i])
        i += 1

    else:
        lista_final.append(lista2[j])
        j += 1


while i < len(lista1):
    lista_final.append(lista1[i])
    i += 1

while j < len(lista2):
    lista_final.append(lista2[j])
    j += 1

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Lista final ordenada: {lista_final}')