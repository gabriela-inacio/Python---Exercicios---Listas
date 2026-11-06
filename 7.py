#Faça um programa que leia uma frase do usuário e exiba quantas palavras ela contém e qual é a palavra
#mais longa. Caso haja empate no tamanho, exiba a primeira que apareceu. Considere que as palavras
#estão separadas por espaços. Exemplo: entrada = "Aprender Python é muito divertido" → 5 palavras,
#palavra mais longa = "Aprender".


frase = input("Digite uma frase: ")

palavras = frase.split()
quantidade = len(palavras)
maior = palavras[0]

i = 0
while i < len(palavras):

    if len(palavras[i]) > len(maior):
        maior = palavras[i]
    i += 1

print(f'Quantidade de palavras: {quantidade}')
print(f'Palavra mais longa: {maior}')

