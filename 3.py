#Leia 10 números inteiros e armazene-os em uma lista. Em seguida, gere uma nova lista contendo apenas
#os elementos sem repetição, mantendo a ordem em que apareceram pela primeira vez. Exiba a lista
#resultante e a quantidade de elementos únicos. Não é permitido usar set(). 
# Exemplo: entrada = [4, 1, 4, 2, 1, 7, 2, 9, 4, 3] → saída = [4, 1, 2, 7, 9, 3]. Total = 6.

i = 0

lista_original = []
lista_sem_repetiçao = []

while i < 10:
    numeros = int(input("Digite numeros inteiros: "))
    lista_original.append(numeros)
    i += 1

i = 0

while i< len(lista_original):
    if lista_original[i] not in lista_sem_repetiçao:
        lista_sem_repetiçao.append(lista_original[i])
    i += 1

print(f'Lista original: {lista_original}')
print(f'Lista sem repetição: {lista_sem_repetiçao}')
print(f'Total de elementos únicos:{len(lista_sem_repetiçao)}')