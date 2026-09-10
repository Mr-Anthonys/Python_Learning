# ============================================================
# Exercício de laços de repetição
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicío 6:
#region
#Lista de compras: crie um programa com for + list  que peça o NOME eo PREÇO de 5 produtos.
#Ao final,  exiba o total gasto e o mais caro

lista_nomes = []#listas vazias
lista_preços = []


for p in range(1, 4):#repetição 
    lista_nomes.append(input(f'Informe o NOME do {p}º produto: ').strip().lower())
    while True:
        entrada_preço = input(f'Informe o PREÇO do {p}º produto R$: ').strip().replace(',','.')#Onde tiver , vou trocar por .
        preço_sem_ponto = entrada_preço.replace('.', '',1)#vou transformar em isdigit(apenas numeros)
        if preço_sem_ponto.isdigit():#verificar se o preço é somente numeros
            lista_preços.append(float(entrada_preço))#se for só numeros a lista append() o preço formato de float()
            break#Para o laço
        else:
            print(f'Preço inválido informe novamente.')
# DAqui pra baixo tudo IA não consegui entender como achar o NOME do produto mais caro


# 1. Encontra o maior preço na lista
maior_preço = max(lista_preços)

# 2. Descobre em qual posição (índice) esse preço está
indice_mais_caro = lista_preços.index(maior_preço)

# 3. Usa o mesmo índice para pegar o nome do produto
produto_mais_caro = lista_nomes[indice_mais_caro]

#Exibindo os resultados
print(f'Total gasto: R$ {sum(lista_preços):.2f}')
print(f'O produto mais caro foi "{produto_mais_caro.title()}" custando R$ {maior_preço:.2f}')
