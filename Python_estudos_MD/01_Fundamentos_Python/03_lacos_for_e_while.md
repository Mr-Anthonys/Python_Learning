# Laços de Repetição em Python (FOR e WHILE) — Guia Completo

## Sumário
1. [O que são laços de repetição](#1-o-que-são-laços-de-repetição)
2. [Laço FOR](#2-laço-for)
3. [A função range()](#3-a-função-range)
4. [Laço WHILE](#4-laço-while)
5. [break, continue e else](#5-break-continue-e-else)
6. [Laços aninhados](#6-laços-aninhados)
7. [enumerate()](#7-enumerate)
8. [zip()](#8-zip)
9. [List comprehensions](#9-list-comprehensions)
10. [Loop infinito controlado](#10-loop-infinito-controlado)
11. [FOR vs WHILE: quando usar cada um](#11-for-vs-while-quando-usar-cada-um)
12. [Boas práticas](#12-boas-práticas)
13. [Erros comuns](#13-erros-comuns)

---

## 1. O que são laços de repetição

Estruturas que executam um bloco de código repetidamente, enquanto uma condição for verdadeira ou enquanto houver itens para percorrer.

---

## 2. Laço FOR

Usado para percorrer (iterar) uma sequência: lista, tupla, string, dicionário, range, etc.

```python
frutas = ["maçã", "banana", "uva"]

for fruta in frutas:
    print(fruta)
# maçã
# banana
# uva
```

Percorrendo uma string:

```python
for letra in "Python":
    print(letra)
```

---

## 3. A função range()

Gera uma sequência de números, muito usada com `for` quando se quer repetir algo um número definido de vezes.

```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (passo de 2)
    print(i)

for i in range(10, 0, -1):  # contagem regressiva: 10, 9, ..., 1
    print(i)
```

---

## 4. Laço WHILE

Repete um bloco **enquanto** uma condição for verdadeira. Diferente do `for`, não sabe de antemão quantas vezes vai repetir.

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
# 0 1 2 3 4
```

Muito usado quando a repetição depende de uma condição externa, como entrada do usuário:

```python
senha = ""
while senha != "1234":
    senha = input("Digite a senha: ")
print("Acesso liberado")
```

---

## 5. break, continue e else

**`break`** — interrompe o laço imediatamente.

```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
# 0 1 2 3 4
```

**`continue`** — pula para a próxima iteração, sem executar o resto do bloco.

```python
for numero in range(5):
    if numero == 2:
        continue
    print(numero)
# 0 1 3 4
```

**`else` em laços** — executa quando o laço termina normalmente (sem `break`). Pouco usado, mas útil em buscas.

```python
numeros = [1, 3, 5, 7]

for n in numeros:
    if n % 2 == 0:
        print("Encontrado par")
        break
else:
    print("Nenhum número par encontrado")  # isso será impresso
```

---

## 6. Laços aninhados

Um laço dentro do outro — comum para trabalhar com matrizes/tabelas.

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)
```

Tabuada usando laços aninhados:

```python
for numero in range(1, 4):
    for multiplicador in range(1, 6):
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    print("---")
```

---

## 7. enumerate()

Permite obter o índice junto com o valor ao percorrer uma sequência.

```python
frutas = ["maçã", "banana", "uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)
# 0 maçã
# 1 banana
# 2 uva

# Pode definir o índice inicial
for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)
# 1 maçã
# 2 banana
# 3 uva
```

---

## 8. zip()

Permite percorrer duas ou mais sequências ao mesmo tempo, em paralelo.

```python
nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")
# Ana tem 25 anos
# Bruno tem 30 anos
# Carla tem 22 anos
```

---

## 9. List comprehensions

Forma resumida e "pythônica" de criar listas usando um `for` em uma única linha.

```python
# Forma tradicional
quadrados = []
for x in range(10):
    quadrados.append(x**2)

# Com list comprehension
quadrados = [x**2 for x in range(10)]

# Com condição
pares = [x for x in range(20) if x % 2 == 0]

# Com condição e else
resultado = ["par" if x % 2 == 0 else "ímpar" for x in range(5)]
```

Também existem versões para dicionários e sets:

```python
# Dict comprehension
quadrados_dict = {x: x**2 for x in range(5)}

# Set comprehension
pares_set = {x for x in range(10) if x % 2 == 0}
```

---

## 10. Loop infinito controlado

Usado quando não se sabe o número de repetições de antemão, controlando a saída manualmente com `break`.

```python
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando == "sair":
        break
    print(f"Você digitou: {comando}")
```

---

## 11. FOR vs WHILE: quando usar cada um

| Situação | Melhor opção |
|---|---|
| Sabe exatamente quantas vezes repetir, ou vai percorrer uma coleção | `for` |
| Repetição depende de uma condição que muda durante a execução | `while` |
| Não sabe quando vai parar (ex: esperar input válido) | `while` |
| Percorrer listas, tuplas, dicionários, strings | `for` |

---

## 12. Boas práticas

- Prefira `for` para percorrer coleções — é mais legível que controlar índice manualmente com `while`
- Evite loops infinitos sem uma condição clara de saída
- Use `enumerate()` em vez de criar um contador manual
- Para criar listas simples a partir de um loop, prefira list comprehension (mais "pythônico")
- Nomeie as variáveis do loop de forma clara (`for aluno in alunos`, não `for x in y`)

---

## 13. Erros comuns

1. **Loop infinito sem `break`** — esquecer de atualizar a variável de controle no `while`.
```python
# ERRADO: contador nunca muda, loop infinito
contador = 0
while contador < 5:
    print(contador)
    # faltou contador += 1
```

2. **Modificar uma lista enquanto itera sobre ela** — pode gerar comportamento inesperado.
```python
# ERRADO
numeros = [1, 2, 3, 4]
for n in numeros:
    if n % 2 == 0:
        numeros.remove(n)  # bagunça a iteração

# CORRETO: iterar sobre uma cópia, ou usar list comprehension
numeros = [n for n in numeros if n % 2 != 0]
```

3. **Confundir `break` com `continue`** — `break` sai do loop; `continue` só pula para a próxima iteração.

4. **Off-by-one em `range()`** — lembrar que `range(5)` vai de 0 a 4, não inclui o 5.

---

## Resumo rápido (cheat sheet)

```python
# FOR
for item in colecao:
    ...

for i in range(inicio, fim, passo):
    ...

# WHILE
while condicao:
    ...

# Controle de fluxo
break       # interrompe o loop
continue    # pula para próxima iteração

# Ferramentas úteis
for i, item in enumerate(lista):
    ...

for a, b in zip(lista1, lista2):
    ...

# List comprehension
resultado = [expressao for item in colecao if condicao]
```
