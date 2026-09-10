# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Exercício 3 - Contador de Letras
# Crie uma função contar_letras(texto).
# Ela deve retornar um dicionário contendo a quantidade de vezes que cada letra aparece.
# Exemplo:
# Entrada:
        # banana

# Saída:

# b = 1
# a = 3
# n = 2


# Conta as letras conforme a regra definida no exercício.
def contar_letras(palavra):
        """Retorna a quantidade de cada letra do valor informado em um dicionário.
    Args:
        palavra (str): texto a ser analisado
    Returns:
        dict: chave = letra, valor = quantidade de ocorrências
    """
        contagem = {}
        for letra in palavra.upper():
                if letra in contagem:
                        contagem[letra] += 1
                else:
                        contagem[letra] = 1
        return contagem
    

#Entrada da palavra.
palavra = input('Informe a palavra p/ contar as letras: ')

#Contador recebe a função que vai contar as letras do que foi salvo na entrada da variavél palavra em forma de dicionário.
contador = contar_letras(palavra)

for letra, qnt in contador.items():#para cada letra(key do dicionario) e qnt(valor do dicionario) do contador (dicionário q recebeu a função) 
        print(f'{letra} = {qnt}') #Exibe os valores como o enunciado pediu



    
    
    