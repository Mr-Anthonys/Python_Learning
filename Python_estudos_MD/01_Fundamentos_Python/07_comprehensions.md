# Comprehensions em Python — Guia Completo

## Sumário
1. [O que é uma comprehension](#1-o-que-é-uma-comprehension)
2. [List comprehension](#2-list-comprehension)
3. [Dict comprehension](#3-dict-comprehension)
4. [Set comprehension](#4-set-comprehension)
5. [Generator expression](#5-generator-expression)
6. [Comprehensions com condição (if)](#6-comprehensions-com-condição-if)
7. [Comprehensions com if-else (ternário)](#7-comprehensions-com-if-else-ternário)
8. [Comprehensions aninhadas](#8-comprehensions-aninhadas)
9. [Comprehension vs loop tradicional: quando usar](#9-comprehension-vs-loop-tradicional-quando-usar)
10. [Performance](#10-performance)
11. [Boas práticas](#11-boas-práticas)
12. [Erros comuns](#12-erros-comuns)

---

## 1. O que é uma comprehension

Uma forma resumida e "pythônica" de criar listas, dicionários ou sets a partir de outra sequência, em uma única linha, substituindo um loop `for` tradicional.

---

## 2. List comprehension

```python
# Forma tradicional
quadrados = []
for x in range(10):
    quadrados.append(x**2)

# Com list comprehension
quadrados = [x**2 for x in range(10)]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# A partir de outra lista
nomes = ["ana", "bruno", "carla"]
maiusculos = [nome.upper() for nome in nomes]
print(maiusculos)  # ['ANA', 'BRUNO', 'CARLA']
```

---

## 3. Dict comprehension

```python
# Forma tradicional
quadrados_dict = {}
for x in range(5):
    quadrados_dict[x] = x**2

# Com comprehension
quadrados_dict = {x: x**2 for x in range(5)}
print(quadrados_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Invertendo chave/valor de um dicionário existente
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in original.items()}
print(invertido)  # {1: 'a', 2: 'b', 3: 'c'}

# A partir de duas listas com zip
nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]
pessoas = {nome: idade for nome, idade in zip(nomes, idades)}
print(pessoas)  # {'Ana': 25, 'Bruno': 30, 'Carla': 22}
```

---

## 4. Set comprehension

```python
numeros = [1, 2, 2, 3, 3, 3, 4]

# Forma tradicional
pares_unicos = set()
for n in numeros:
    if n % 2 == 0:
        pares_unicos.add(n)

# Com comprehension
pares_unicos = {n for n in numeros if n % 2 == 0}
print(pares_unicos)  # {2, 4}
```

---

## 5. Generator expression

Parecida com list comprehension, mas usa `()` em vez de `[]`, e gera os valores **sob demanda** (economiza memória — não cria a lista inteira de uma vez).

```python
# List comprehension: cria tudo na memória de uma vez
lista = [x**2 for x in range(1000000)]

# Generator expression: gera um valor por vez, sob demanda
gerador = (x**2 for x in range(1000000))

print(next(gerador))  # 0
print(next(gerador))  # 1

# Muito usado dentro de funções como sum(), max(), any()
total = sum(x**2 for x in range(10))
existe_par = any(x % 2 == 0 for x in range(10))
```

---

## 6. Comprehensions com condição (if)

```python
numeros = range(20)

pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Múltiplas condições
divisiveis = [x for x in numeros if x % 2 == 0 if x % 3 == 0]
print(divisiveis)  # [0, 6, 12, 18]
```

---

## 7. Comprehensions com if-else (ternário)

Quando o `if` decide o **valor**, e não se o item entra ou não na lista, ele vem **antes** do `for`:

```python
numeros = range(10)

resultado = ["par" if x % 2 == 0 else "ímpar" for x in numeros]
print(resultado)
# ['par', 'ímpar', 'par', 'ímpar', ...]
```

**Diferença importante:**

```python
# if DEPOIS do for -> FILTRA itens
pares = [x for x in range(10) if x % 2 == 0]

# if ANTES do for (com else) -> TRANSFORMA o valor, mantém todos os itens
classificados = [x if x % 2 == 0 else -x for x in range(10)]
```

---

## 8. Comprehensions aninhadas

```python
# Achatar uma matriz (lista de listas) em uma lista única
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
achatada = [valor for linha in matriz for valor in linha]
print(achatada)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Criar uma matriz com comprehension
matriz_nova = [[i * j for j in range(3)] for i in range(3)]
print(matriz_nova)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Combinando duas listas (produto cartesiano)
cores = ["vermelho", "azul"]
tamanhos = ["P", "M", "G"]
combinacoes = [(cor, tamanho) for cor in cores for tamanho in tamanhos]
print(combinacoes)
# [('vermelho', 'P'), ('vermelho', 'M'), ..., ('azul', 'G')]
```

---

## 9. Comprehension vs loop tradicional: quando usar

| Situação | Recomendação |
|---|---|
| Transformação simples de uma lista | Comprehension |
| Lógica com múltiplas condições complexas | Loop tradicional (mais legível) |
| Precisa de efeitos colaterais (print, log, etc.) dentro do loop | Loop tradicional |
| Trabalhar com grandes volumes de dados, economizando memória | Generator expression |

```python
# Comprehension muito complexa - prefira um loop tradicional
resultado = [funcao_complexa(x) for x in dados if condicao1(x) if condicao2(x) if not condicao3(x)]
# Mais legível como loop:
resultado = []
for x in dados:
    if condicao1(x) and condicao2(x) and not condicao3(x):
        resultado.append(funcao_complexa(x))
```

---

## 10. Performance

Comprehensions costumam ser um pouco mais rápidas que loops tradicionais equivalentes com `.append()`, pois são otimizadas internamente pelo Python. Generator expressions economizam memória ao lidar com grandes volumes de dados, pois não armazenam tudo de uma vez.

```python
import sys

lista = [x for x in range(100000)]
gerador = (x for x in range(100000))

print(sys.getsizeof(lista))    # tamanho considerável em memória
print(sys.getsizeof(gerador))  # tamanho fixo, muito menor
```

---

## 11. Boas práticas

- Use comprehensions para transformações e filtros **simples e diretos**
- Se a comprehension precisar de mais de uma linha pra ficar legível, prefira um loop `for` tradicional
- Use generator expressions quando só for percorrer os dados uma vez (economiza memória)
- Nomeie bem a variável usada na comprehension, mesmo sendo código curto

---

## 12. Erros comuns

1. **Comprehensions longas e ilegíveis** — quando fica difícil de ler rapidamente, é sinal de usar um loop tradicional.
2. **Confundir a posição do `if`** — filtro (depois do `for`) vs condicional de valor (antes do `for`, com `else`).
3. **Usar list comprehension quando um generator seria mais eficiente** (ex: dentro de `sum()`, `any()`, `all()` — não precisa dos colchetes).
```python
# Desnecessário criar a lista inteira:
total = sum([x**2 for x in range(1000000)])

# Mais eficiente com generator (sem colchetes):
total = sum(x**2 for x in range(1000000))
```
4. **Esquecer que dict/set comprehension não mantêm ordem por índice** (dict mantém ordem de inserção desde Python 3.7+, mas set não é ordenado).

---

## Resumo rápido (cheat sheet)

```python
# List comprehension
[expressao for item in iteravel]
[expressao for item in iteravel if condicao]
[expr1 if condicao else expr2 for item in iteravel]

# Dict comprehension
{chave: valor for item in iteravel}

# Set comprehension
{expressao for item in iteravel}

# Generator expression
(expressao for item in iteravel)

# Aninhada
[valor for linha in matriz for valor in linha]
```
