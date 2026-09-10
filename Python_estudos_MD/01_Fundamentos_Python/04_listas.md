# Listas em Python — Guia Completo (Básico ao Avançado)

## Sumário
1. [O que é uma lista](#1-o-que-é-uma-lista)
2. [Criando listas](#2-criando-listas)
3. [Acessando elementos e slicing](#3-acessando-elementos-e-slicing)
4. [Métodos essenciais](#4-métodos-essenciais)
5. [Adicionando e removendo itens](#5-adicionando-e-removendo-itens)
6. [Ordenação](#6-ordenação)
7. [Listas aninhadas (matrizes)](#7-listas-aninhadas-matrizes)
8. [Copiando listas (cópia rasa vs profunda)](#8-copiando-listas-cópia-rasa-vs-profunda)
9. [List comprehensions](#9-list-comprehensions)
10. [Funções úteis com listas](#10-funções-úteis-com-listas)
11. [Listas vs Tuplas vs Sets](#11-listas-vs-tuplas-vs-sets)
12. [Boas práticas](#12-boas-práticas)
13. [Erros comuns](#13-erros-comuns)

---

## 1. O que é uma lista

Uma coleção **ordenada** e **mutável** de elementos, podendo conter tipos diferentes (números, strings, outras listas, etc.).

---

## 2. Criando listas

```python
lista_vazia = []
numeros = [1, 2, 3, 4, 5]
mista = [1, "texto", 3.14, True]

# Usando a função list()
lista_de_tupla = list((1, 2, 3))
lista_de_string = list("abc")  # ['a', 'b', 'c']

# Lista com valores repetidos
zeros = [0] * 5  # [0, 0, 0, 0, 0]
```

---

## 3. Acessando elementos e slicing

```python
frutas = ["maçã", "banana", "uva", "laranja", "manga"]

print(frutas[0])    # maçã
print(frutas[-1])   # manga (último item)

print(frutas[1:3])  # ['banana', 'uva']
print(frutas[:2])   # ['maçã', 'banana']
print(frutas[2:])   # ['uva', 'laranja', 'manga']
print(frutas[::-1]) # lista invertida
print(frutas[::2])  # ['maçã', 'uva', 'manga'] — passo 2
```

---

## 4. Métodos essenciais

```python
frutas = ["maçã", "banana", "uva"]

print(len(frutas))          # 3 — tamanho da lista
print("uva" in frutas)      # True — verifica se existe
print(frutas.index("uva"))  # 2 — posição do item
print(frutas.count("uva"))  # 1 — quantas vezes aparece
```

---

## 5. Adicionando e removendo itens

```python
frutas = ["maçã", "banana"]

# Adicionar
frutas.append("uva")           # adiciona no final: ['maçã', 'banana', 'uva']
frutas.insert(1, "morango")    # insere na posição 1: ['maçã', 'morango', 'banana', 'uva']
frutas.extend(["kiwi", "pera"]) # adiciona vários itens no final

# Remover
frutas.remove("banana")   # remove pelo VALOR (primeira ocorrência)
item = frutas.pop()       # remove e retorna o ÚLTIMO item
item = frutas.pop(0)      # remove e retorna o item do índice 0
del frutas[0]             # remove pelo índice, sem retornar
frutas.clear()            # remove todos os itens, lista fica vazia []
```

**Diferença entre `remove`, `pop` e `del`:**

| Método | Como funciona |
|---|---|
| `remove(valor)` | Remove pelo valor (erro se não existir) |
| `pop(indice)` | Remove pelo índice e **retorna** o item removido |
| `del lista[indice]` | Remove pelo índice, não retorna nada |

---

## 6. Ordenação

```python
numeros = [5, 2, 8, 1, 9]

numeros.sort()             # ordena a própria lista (in-place): [1, 2, 5, 8, 9]
numeros.sort(reverse=True) # ordem decrescente: [9, 8, 5, 2, 1]

# sorted() retorna uma NOVA lista, sem alterar a original
nova_lista = sorted(numeros)

# Ordenar por critério customizado
palavras = ["banana", "uva", "abacaxi"]
palavras.sort(key=len)  # ordena pelo tamanho da string
print(palavras)  # ['uva', 'banana', 'abacaxi']

# Ordenar lista de dicionários/tuplas por um campo específico
pessoas = [("Ana", 25), ("Bruno", 20), ("Carla", 30)]
pessoas.sort(key=lambda p: p[1])  # ordena pela idade
```

---

## 7. Listas aninhadas (matrizes)

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1])      # [4, 5, 6]
print(matriz[1][2])   # 6

# Percorrendo uma matriz
for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()
```

---

## 8. Copiando listas (cópia rasa vs profunda)

⚠️ Um erro comum: apenas atribuir `lista2 = lista1` NÃO cria uma cópia — cria uma segunda referência para a mesma lista.

```python
original = [1, 2, 3]
referencia = original      # NÃO é cópia!
referencia.append(4)
print(original)  # [1, 2, 3, 4] — a original também mudou!

# Formas corretas de copiar (cópia rasa)
copia1 = original.copy()
copia2 = list(original)
copia3 = original[:]

copia1.append(5)
print(original)  # [1, 2, 3, 4] — não foi afetada
```

Para listas aninhadas, cópia rasa não é suficiente (as listas internas ainda são compartilhadas):

```python
import copy

matriz_original = [[1, 2], [3, 4]]
copia_rasa = matriz_original.copy()
copia_rasa[0].append(99)
print(matriz_original)  # [[1, 2, 99], [3, 4]] — foi afetada!

copia_profunda = copy.deepcopy(matriz_original)
copia_profunda[0].append(100)
print(matriz_original)  # não é afetada pela cópia profunda
```

---

## 9. List comprehensions

```python
quadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
resultado = ["par" if x % 2 == 0 else "ímpar" for x in range(5)]

# Achatando uma lista de listas (matriz -> lista única)
matriz = [[1, 2], [3, 4], [5, 6]]
achatada = [valor for linha in matriz for valor in linha]
print(achatada)  # [1, 2, 3, 4, 5, 6]
```

---

## 10. Funções úteis com listas

```python
numeros = [4, 2, 8, 1, 9]

print(sum(numeros))     # 24
print(max(numeros))     # 9
print(min(numeros))     # 1
print(len(numeros))     # 5

# map: aplica uma função a cada item
dobrados = list(map(lambda x: x * 2, numeros))

# filter: filtra itens que satisfazem uma condição
maiores_que_3 = list(filter(lambda x: x > 3, numeros))

# any/all
print(any(x > 5 for x in numeros))  # True (pelo menos um maior que 5)
print(all(x > 0 for x in numeros))  # True (todos maiores que 0)
```

---

## 11. Listas vs Tuplas vs Sets

| Estrutura | Ordenada | Mutável | Permite duplicados |
|---|---|---|---|
| Lista `[]` | Sim | Sim | Sim |
| Tupla `()` | Sim | Não | Sim |
| Set `{}` | Não | Sim | Não |

---

## 12. Boas práticas

- Use listas quando os dados podem crescer, encolher ou ser reordenados
- Prefira `sorted()` quando quiser manter a lista original intacta; use `.sort()` quando não precisar dela
- Para copiar listas, use `.copy()`, `list()` ou `[:]` — nunca apenas `=`
- Use list comprehension para transformações simples, mas evite comprehensions muito complexas (prejudica legibilidade)
- Evite modificar uma lista enquanto itera sobre ela diretamente

---

## 13. Erros comuns

1. **Achar que `lista2 = lista1` cria uma cópia** — cria apenas uma segunda referência.
2. **Modificar a lista durante um loop `for`**, causando itens pulados.
```python
# ERRADO
numeros = [1, 2, 3, 4]
for n in numeros:
    if n % 2 == 0:
        numeros.remove(n)  # comportamento inesperado
```
3. **Confundir `remove()` (por valor) com `pop()` (por índice)**.
4. **Usar `append()` quando queria `extend()`**:
```python
lista = [1, 2, 3]
lista.append([4, 5])   # [1, 2, 3, [4, 5]] — adiciona a lista inteira como item
lista.extend([4, 5])   # [1, 2, 3, 4, 5] — adiciona cada item individualmente
```
5. **IndexError** ao acessar um índice que não existe.

---

## Resumo rápido (cheat sheet)

```python
# Criação
lista = [1, 2, 3]

# Acesso e slicing
lista[0]
lista[1:3]
lista[::-1]

# Adicionar
lista.append(x)
lista.insert(i, x)
lista.extend([...])

# Remover
lista.remove(valor)
lista.pop(i)
del lista[i]
lista.clear()

# Ordenação
lista.sort()
sorted(lista)

# Cópia
copia = lista.copy()  # ou list(lista) ou lista[:]

# Comprehension
nova = [expressao for item in lista if condicao]
```
