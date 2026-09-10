# Tuplas em Python — Guia Completo (Básico ao Avançado)

## Sumário
1. [O que é uma tupla](#1-o-que-é-uma-tupla)
2. [Criando tuplas](#2-criando-tuplas)
3. [Acessando elementos (indexação)](#3-acessando-elementos-indexação)
4. [Slicing (fatiamento)](#4-slicing-fatiamento)
5. [Imutabilidade](#5-imutabilidade)
6. [Métodos de tupla](#6-métodos-de-tupla)
7. [Tuple unpacking (desempacotamento)](#7-tuple-unpacking-desempacotamento)
8. [Tuplas aninhadas](#8-tuplas-aninhadas)
9. [Tuplas nomeadas (namedtuple)](#9-tuplas-nomeadas-namedtuple)
10. [Tupla vs Lista: quando usar](#10-tupla-vs-lista-quando-usar)
11. [Boas práticas](#11-boas-práticas)
12. [Erros comuns](#12-erros-comuns)

---

## 1. O que é uma tupla

Uma coleção **ordenada** e **imutável** de elementos. Uma vez criada, não pode ser alterada (não é possível adicionar, remover ou modificar itens).

---

## 2. Criando tuplas

```python
tupla_vazia = ()
cores = ("vermelho", "verde", "azul")
numeros = (1, 2, 3, 4, 5)
mista = (1, "texto", 3.14, True)

# Parênteses são opcionais (mas recomendados para clareza)
tupla_sem_parenteses = 1, 2, 3

# Tupla com um único elemento precisa da vírgula!
tupla_um_item = (5,)     # isso é uma tupla
nao_e_tupla = (5)        # isso é apenas um número inteiro entre parênteses

# Usando a função tuple()
tupla_de_lista = tuple([1, 2, 3])
tupla_de_string = tuple("abc")  # ('a', 'b', 'c')
```

---

## 3. Acessando elementos (indexação)

```python
cores = ("vermelho", "verde", "azul")

print(cores[0])   # vermelho (primeiro item)
print(cores[-1])  # azul (último item)
print(cores[1])   # verde
```

Índices começam em `0`. Índices negativos contam a partir do final.

---

## 4. Slicing (fatiamento)

Extrai uma "fatia" da tupla, retornando uma nova tupla.

```python
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numeros[2:5])    # (2, 3, 4)
print(numeros[:4])     # (0, 1, 2, 3) — do início até o índice 4 (exclusivo)
print(numeros[6:])     # (6, 7, 8, 9) — do índice 6 até o final
print(numeros[::2])    # (0, 2, 4, 6, 8) — passo 2
print(numeros[::-1])   # tupla invertida
```

---

## 5. Imutabilidade

Uma vez criada, os elementos de uma tupla **não podem ser alterados**.

```python
cores = ("vermelho", "verde", "azul")
cores[0] = "amarelo"  # ERRO: TypeError
```

Isso torna tuplas mais seguras para representar dados que não devem mudar (ex: coordenadas, configurações fixas) e também um pouco mais rápidas/leves em memória que listas.

⚠️ **Detalhe importante**: se a tupla contém um objeto mutável (como uma lista), o conteúdo desse objeto ainda pode ser alterado:

```python
tupla_com_lista = (1, 2, [3, 4])
tupla_com_lista[2].append(5)
print(tupla_com_lista)  # (1, 2, [3, 4, 5]) — funcionou, pois a lista interna é mutável
```

---

## 6. Métodos de tupla

Tuplas têm poucos métodos, justamente por serem imutáveis.

```python
numeros = (1, 2, 3, 2, 4, 2)

print(numeros.count(2))   # 3 — conta quantas vezes o valor aparece
print(numeros.index(3))   # 2 — retorna o índice da primeira ocorrência

# Funções embutidas que funcionam com tuplas
print(len(numeros))       # 6
print(max(numeros))       # 4
print(min(numeros))       # 1
print(sum(numeros))       # 14
print(sorted(numeros))    # [1, 2, 2, 2, 3, 4] — retorna uma LISTA ordenada
```

---

## 7. Tuple unpacking (desempacotamento)

Uma das funcionalidades mais usadas — permite atribuir os elementos de uma tupla diretamente a variáveis.

```python
pessoa = ("Ana", 25, "Engenheira")
nome, idade, profissao = pessoa

print(nome)       # Ana
print(idade)      # 25
print(profissao)  # Engenheira
```

Trocar valores entre variáveis (clássico truque do Python):

```python
a = 1
b = 2
a, b = b, a
print(a, b)  # 2 1
```

Usando `*` para capturar "o resto":

```python
numeros = (1, 2, 3, 4, 5)
primeiro, *meio, ultimo = numeros

print(primeiro)  # 1
print(meio)      # [2, 3, 4]  (vira uma lista)
print(ultimo)    # 5
```

Muito comum ao retornar múltiplos valores de uma função:

```python
def calcular(a, b):
    return a + b, a - b, a * b  # retorna uma tupla

soma, subtracao, multiplicacao = calcular(10, 3)
print(soma, subtracao, multiplicacao)  # 13 7 30
```

---

## 8. Tuplas aninhadas

Tuplas podem conter outras tuplas.

```python
matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(matriz[1])       # (4, 5, 6)
print(matriz[1][2])    # 6

for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
```

---

## 9. Tuplas nomeadas (namedtuple)

Do módulo `collections` — cria tuplas onde os campos têm nome, deixando o código mais legível que acessar por índice.

```python
from collections import namedtuple

Ponto = namedtuple("Ponto", ["x", "y"])

p1 = Ponto(3, 4)
print(p1.x, p1.y)   # 3 4
print(p1[0], p1[1])  # também funciona por índice: 3 4

# Muito usado para representar registros simples
Pessoa = namedtuple("Pessoa", "nome idade profissao")
ana = Pessoa("Ana", 25, "Engenheira")
print(ana.nome)  # Ana
```

---

## 10. Tupla vs Lista: quando usar

| Tupla | Lista |
|---|---|
| Imutável | Mutável |
| Mais rápida e leve em memória | Um pouco mais pesada |
| Dados que não devem mudar (coordenadas, configs) | Dados que serão modificados (adicionar/remover itens) |
| Pode ser usada como chave de dicionário | Não pode ser usada como chave de dicionário |

```python
# Tupla pode ser chave de dicionário, lista não pode
coordenadas = {(0, 0): "origem", (1, 1): "ponto A"}

# Isso geraria erro:
# coordenadas2 = {[0, 0]: "origem"}  # TypeError: unhashable type: 'list'
```

---

## 11. Boas práticas

- Use tuplas para dados que representam um "registro fixo" (ex: coordenada `(x, y)`, data `(dia, mes, ano)`)
- Prefira tuplas a listas quando a coleção não precisa mudar — deixa a intenção do código mais clara
- Use `namedtuple` quando quiser dar nomes aos campos, melhorando a legibilidade
- Aproveite o unpacking para retornar múltiplos valores de funções de forma elegante

---

## 12. Erros comuns

1. **Esquecer a vírgula em tupla de um elemento**: `(5)` é apenas um número, `(5,)` é uma tupla.
2. **Tentar modificar uma tupla diretamente** — gera `TypeError`.
3. **Confundir tupla com lista na hora de escolher a estrutura** — se os dados vão mudar, use lista.
4. **Desempacotar com número errado de variáveis**:
```python
a, b = (1, 2, 3)  # ERRO: ValueError: too many values to unpack
```

---

## Resumo rápido (cheat sheet)

```python
# Criação
t = (1, 2, 3)
t_um_item = (5,)

# Acesso
t[0]        # primeiro elemento
t[-1]       # último elemento
t[1:3]      # slice

# Métodos
t.count(valor)
t.index(valor)

# Unpacking
a, b, c = t
primeiro, *resto = t

# Namedtuple
from collections import namedtuple
Ponto = namedtuple("Ponto", ["x", "y"])
p = Ponto(1, 2)
```
