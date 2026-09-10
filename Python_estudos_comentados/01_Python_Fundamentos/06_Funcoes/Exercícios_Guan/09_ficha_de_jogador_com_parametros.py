# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Função ficha(), receba 2 param: opcionais. NOME e GOLS q um jogador marcou.
#Devera exibir a ficha mesmo se algum param: não foi informado.


# Organiza e exibe as informações principais do objeto.
def ficha(nome=('<DESCONHECIDO>'), gols=0):
    pessoa = {}
    pessoa["nome"] = nome
    pessoa["gols"] = gols
    return (f'Jogador {pessoa["nome"].title()} fez {pessoa["gols"]} no campeonato.')
   


nome_input = input(f'NOME: ')
gols_input = input(f'QUANTOS GOLS: ')

if nome_input and gols_input:# 1) os DOIS foram informados
    print(ficha(nome_input, int(gols_input)))   

elif nome_input:# 2) só o NOME foi informado
    print(ficha(nome=nome_input))                

elif gols_input:# 3) só o GOLS foi informado

    print(ficha(gols=int(gols_input)))            
else:
    print(ficha())    




