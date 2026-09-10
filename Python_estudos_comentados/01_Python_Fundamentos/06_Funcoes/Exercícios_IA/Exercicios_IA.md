Exercício 4 - Validador de CPF

Crie uma função validar_cpf(cpf).

Ela deve verificar:

* possui exatamente 11 caracteres?
* todos são números?

Se sim, retorne True.

Caso contrário, retorne False.

Não é necessário validar os dígitos verificadores.

⸻

Exercício 5 - Sistema Bancário

Crie as funções:

depositar()

sacar()

consultar_saldo()

Utilize uma variável chamada saldo.

Monte um menu:

1 - Depositar
2 - Sacar
3 - Consultar saldo
4 - Sair

O menu deve permanecer funcionando até o usuário escolher sair.

⸻



⸻

Exercício 7 - Senha Forte

Crie uma função senha_forte().

Ela deve retornar True somente se a senha possuir:

* pelo menos 8 caracteres
* uma letra maiúscula
* uma letra minúscula
* um número
* um caractere especial

Caso contrário, False.

Exemplo:

Senha:

Python123@

Resultado:

Senha forte.

⸻

Exercício 8 - Frequência de Palavras

Crie uma função que receba uma frase.

Ela deve informar quantas vezes cada palavra apareceu.

Exemplo:

Entrada:

python é legal python é divertido

Resultado:

python = 2

é = 2

legal = 1

divertido = 1

⸻

Exercício 9 - Ordenação

Crie uma função que receba uma lista de números.

Ela deve retornar:

Lista em ordem crescente.

Lista em ordem decrescente.

A lista original não pode ser alterada.

Exemplo:

Lista:

7
3
9
2
8

Resultado:

Crescente:

2
3
7
8
9

Decrescente:

9
8
7
3
2

⸻

Exercício 10 - Login

Crie duas funções.

cadastrar()

login()

Cadastre um usuário e uma senha em um dicionário.

Depois permita que o usuário faça login.

Se o usuário não existir:

Usuário inexistente.

Se a senha estiver errada:

Senha incorreta.

Caso esteja tudo correto:

Login realizado com sucesso.

==================================================

DESAFIO 1 - INVENTÁRIO DE JOGOS

Cada jogo deve possuir:

Nome

Gênero

Horas jogadas

Crie funções para:

Adicionar jogo

Remover jogo

Pesquisar jogo

Listar todos

Mostrar o jogo mais jogado

==================================================

DESAFIO 2 - AGENDA

Cada contato deve possuir:

Nome

Telefone

E-mail

Crie funções para:

Adicionar contato

Editar contato

Excluir contato

Pesquisar contato

Listar todos em ordem alfabética

==================================================

DESAFIO 3 - ESTATÍSTICAS

Crie uma função que receba uma lista de números.

Ela deve retornar:

Maior número

Menor número

Média

Mediana

Quantidade de elementos

Soma total

Lista dos números pares

Lista dos números ímpares

==================================================

DESAFIO 4 - CYBERSEGURANÇA

Crie uma lista contendo as 20 senhas mais comuns.

Exemplo:

123456

123456789

admin

qwerty

password

123123

…

Crie uma função verificar_senha().

Se a senha estiver nessa lista:

Senha extremamente fraca.

Caso contrário:

Senha não encontrada na lista de senhas comuns.

==================================================

DESAFIO 5 - SCANNER DE ARQUIVOS

Receba uma lista contendo:

foto.jpg

virus.exe

texto.txt

script.py

planilha.xlsx

backup.zip

musica.mp3

A função deve agrupar os arquivos pela extensão.

Resultado esperado:

jpg:

* foto.jpg

exe:

* virus.exe

txt:

* texto.txt

py:

* script.py

xlsx:

* planilha.xlsx

zip:

* backup.zip

mp3:

* musica.mp3

==================================================

DESAFIO FINAL

Crie um sistema completo utilizando:

✓ Funções

✓ Listas

✓ Tuplas

✓ Dicionários

✓ Laços

✓ Condições

✓ Menu principal

✓ Tratamento de erros

Escolha um dos temas:

* Biblioteca
* Mercado
* Loja
* RPG
* Hospital
* Controle Financeiro
* Estoque
* Academia
* Gerenciador de Tarefas
* Locadora de Filmes

⸻
Nível básico — sintaxe e retorno

1. Crie uma função saudacao(nome) que retorna a string "Olá, {nome}!".

2. Crie uma função soma(a, b) que retorna a soma dos dois valores.

3. Crie uma função eh_par(numero) que retorna True se o número for par e False se for ímpar.

Nível intermediário — parâmetros padrão e múltiplos argumentos

4. Crie uma função apresentar(nome, idade=18) onde idade tem valor padrão 18. Chame ela duas vezes: uma passando só o nome, outra passando nome e idade.

5. Crie uma função media(*numeros) que aceita uma quantidade variável de números e retorna a média deles. (Ex: media(2, 4, 6) deve retornar 4.0)

6. Crie uma função criar_perfil(**dados) que aceita **kwargs e imprime cada chave/valor recebido. (Ex: criar_perfil(nome="Ana", idade=25, cidade="SP"))

Nível avançado — combinando com o que você já viu (loops + funções)

7. Crie uma função contar_vogais(texto) que percorre a string com um for e retorna quantas vogais ela tem.

8. Crie uma função numeros_primos(limite) que retorna uma lista com todos os números primos até limite.

Aplicado ao seu projeto (funções sem retorno, "ação")

9. Reescreva a função barra_carregando (que fizemos antes) mas agora com um parâmetro extra velocidade que controla o sleep. Ex: barra_carregando(total=50, velocidade=0.05).

10. Crie uma função mensagem_sucesso(texto) usando rich que imprime o texto em verde e negrito (pesquise rich.console.Console e o print com markup, ex: console.print(f"[bold green]{texto}[/bold green]")).