# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicio 9 
#region 
# Procurando o Dono da Posição:
#Crie um programa que peça o nome de 5 alunos e suas respectivas notas finais
#(use duas listas separadas, igual ao exercício do mercado).
#No final, peça ao usuário para digitar o nome de um aluno. 
#O programa deve buscar esse aluno e exibir a nota dele. 
#Se o aluno não existir, avise-o.

lista_nomes = []
lista_notas = []

for item in range(1 , 3):
    lista_nomes.append(input(f'Informe o NOME do {item}º aluno: ').strip())
    lista_notas.append(input(f'Informa a NOTA do {item}º aluno: ').strip())

aluno = input(f'Qual aluno está buscando na lista?: ').strip().title()
if aluno in lista_nomes:
    posiçao_nome = lista_nomes.index(aluno)
    print(f'O aluno {aluno} está na lista.')   
else:
    print(f'O "{aluno}" informado não esta na lista.')
