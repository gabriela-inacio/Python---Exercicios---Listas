#Implemente um sistema simples de votação:
#a) O usuário informa quantos candidatos existem (mínimo 2) e em seguida digita o nome de cada um, que
#serão armazenados em uma lista.
#b) Em seguida, votos são registrados um por um: a cada voto, o usuário digita o nome de um candidato. Se o
#nome digitado não existir entre os candidatos, exibir "Voto inválido" e ignorar (não conta). A votação termina
#quando o usuário digita "fim".
#c) Ao final, exibir:
#● o total de votos válidos
#● a quantidade de votos de cada candidato
#● o(s) vencedor(es) e o percentual de votos dele(s), com 2 casas decimais
#● em caso de empate, exibir todos os vencedores empatados

candidatos = []
votos = []
quantidade =  int(input("Informe a quantidade de candidatos: "))

i = 0
while i < quantidade:
    nomes = input("Informe o nome do candidato: ")
    candidatos.append(nomes)
    votos.append(0)
    i += 1

while True:

    voto = input("Informe o nome do candidato que deseja votar(ou fim para encerrar): ")

    if voto == 'fim':
        break

    if voto in candidatos:
        indice = candidatos.index(voto)
        votos[indice] += 1
    else:
        print("Voto inválido!")

print("\nResultado da votação:")

i = 0
while i < len(candidatos):
    print(f"{candidatos[i]}: {votos[i]} voto(s)")
    i += 1

total = sum(votos)
print(f"\nTotal de votos válidos: {total}")


print("\nVencedor(es):")
maior = max(votos)

i = 0
while i < len(candidatos):

    if votos[i] == maior:
        porcentagem = (votos[i] / total) * 100
        print(f"{candidatos[i]} - {porcentagem:.2f}% dos votos")
    i += 1