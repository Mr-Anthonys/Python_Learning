# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicio 5. (Listas compostas e acesso com indices)

#Leia nome e 2 notas de varios alunos e guarde em 1 lista composta
#mostre um boletim com a media de cada aluno
#permita q o usuario possa mostrar as notas de cada aluno individualmente.
  
alunos = [[],[],[],[]]#nome, nota1, nota2, media


r = 'Ss'
while r not in 'Nn':
    nome = str(input('Informe o NOME: ').lower())
    alunos[0].append(nome)

    nota_1 = float(input(f'Informe a 1º nota de {nome}: '))
    alunos[1].append(nota_1)

    nota_2 = float(input(f'Informe a 2º nota de {nome}: '))
    alunos[2].append(nota_2)

    media = (nota_1 + nota_2) / 2
    alunos[3].append(media)
    r = input(f'Deseja continuar [S/N]: ').strip().lower()



print('='*40)
print(f'{"BOLETIM":^40}')
print('='*40)
cont = 0
for nome in alunos[0]:
    print(f'-'*40)    
    print(f'A media de {nome} foi {alunos[3][cont]}')    
    cont += 1

aluno_individual = str(input(f'Informe o aluno para ver suas notas: ').lower())

if aluno_individual in alunos[0]:
    posição = alunos[0].index(aluno_individual)
else:
    print(f'Aluno não encontrado.')

print(f'{aluno_individual.title()}1º NOTA: ({alunos[1][posição]}).')
print(f'{aluno_individual.title()}2º NOTA: ({alunos[2][posição]}).')