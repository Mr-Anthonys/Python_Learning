# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Exercício 1 - Cadastro de Pessoa

# Crie uma função chamada cadastrar_pessoa() que receba como parâmetros:
# * nome
# * idade
# * profissão

# Ela deve retornar um dicionário contendo essas informações.
# Depois imprima o dicionário de forma organizada.
# Exemplo de saída:

# Nome: João
# Idade: 25
# Profissão: Programador

# Realiza o cadastro e organiza os dados das pessoas.
def cadastrar_pessoas(n, i, p):
    pessoas = dict()
    pessoas["nome"] = n
    pessoas["idade"] = i
    pessoas["profissão"] = p
    return pessoas


#- programa principal

n = input('NOME: ').strip()
i = input('IDADE: ')
p = input('PROFISSÃO: ')

pessoas_dict = cadastrar_pessoas(n, i, p)

print(f'Dicionário ---> {pessoas_dict}')

print(f'Dicionário organizado: ')
for k, v in pessoas_dict.items():
    print(f'{k} : {v}')

