#8. Implemente um programa que avalie a força de uma senha digitada pelo usuário, segundo as seguintes
#regras:
#● Possuir no mínimo 8 caracteres
#● Conter pelo menos uma letra maiúscula
#● Conter pelo menos uma letra minúscula
#● Conter pelo menos um dígito (0–9)
#● Conter pelo menos um caractere especial dentre: ! @ # $ % & * ?

#A classificação final deve ser:
#● 5 critérios atendidos → "Senha forte"#
# ● 3 ou 4 critérios atendidos → "Senha média"
#● Menos que 3 critérios → "Senha fraca"
#O programa deve exibir a classificação e, em seguida, listar quais critérios não foram atendidos (caso haja
#algum).


senha = input("Digite uma senha: ")

criterios = 0
maiuscula = False
minuscula = False
numero = False
especial = False

if len(senha) >= 8:
    criterios += 1
i = 0

while i < len(senha):

    caractere = senha[i]

    if caractere.isupper():
        maiuscula = True

    if caractere.islower():
        minuscula = True

    if caractere.isdigit():
        numero = True

    if caractere in "!@#$%&*?":
        especial = True
    i += 1

if maiuscula:
    criterios += 1
if minuscula:
    criterios += 1
if numero:
    criterios += 1
if especial:
    criterios += 1


if criterios == 5:
    print("Senha forte")
elif criterios >= 3:
    print("Senha média")
else:
    print("Senha fraca")


print("\nCritérios não atendidos:")

if len(senha) < 8:
    print("- Mínimo de 8 caracteres")
if not maiuscula:
    print("- Pelo menos uma letra maiúscula")
if not minuscula:
    print("- Pelo menos uma letra minúscula")
if not numero:
    print("- Pelo menos um número")
if not especial:
    print("- Pelo menos um caractere especial (! @ # $ % & * ?)")

