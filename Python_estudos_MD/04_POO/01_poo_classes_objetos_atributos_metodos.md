# Programação Orientada a Objetos (POO) em Python — Guia Completo

## Sumário
1. [O que é POO](#1-o-que-é-poo)
2. [Classes e objetos](#2-classes-e-objetos)
3. [O método __init__ e self](#3-o-método-__init__-e-self)
4. [Atributos e métodos](#4-atributos-e-métodos)
5. [Encapsulamento](#5-encapsulamento)
6. [Herança](#6-herança)
7. [Polimorfismo](#7-polimorfismo)
8. [Métodos especiais (dunder methods)](#8-métodos-especiais-dunder-methods)
9. [Atributos e métodos de classe (static/classmethod)](#9-atributos-e-métodos-de-classe-staticclassmethod)
10. [Properties (getters/setters pythônicos)](#10-properties-getterssetters-pythônicos)
11. [Classes abstratas](#11-classes-abstratas)
12. [Composição vs Herança](#12-composição-vs-herança)
13. [Boas práticas](#13-boas-práticas)
14. [Erros comuns](#14-erros-comuns)

---

## 1. O que é POO

Paradigma de programação que organiza o código em torno de **objetos**, que combinam dados (atributos) e comportamentos (métodos). Os quatro pilares são: **encapsulamento, herança, polimorfismo e abstração**.

---

## 2. Classes e objetos

- **Classe**: um "molde" que define atributos e comportamentos.
- **Objeto (instância)**: uma "unidade" criada a partir da classe.

```python
class Cachorro:
    pass

meu_cachorro = Cachorro()  # meu_cachorro é uma instância (objeto) da classe Cachorro
```

---

## 3. O método __init__ e self

`__init__` é o construtor — executado automaticamente ao criar um objeto. `self` representa a própria instância.

```python
class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

rex = Cachorro("Rex", "Labrador")
print(rex.nome)  # Rex
print(rex.raca)  # Labrador
```

---

## 4. Atributos e métodos

```python
class Cachorro:
    especie = "Canis familiaris"  # atributo de classe (compartilhado por todas instâncias)

    def __init__(self, nome, idade):
        self.nome = nome    # atributo de instância (próprio de cada objeto)
        self.idade = idade

    def latir(self):        # método (comportamento)
        return f"{self.nome} está latindo: Au au!"

    def aniversario(self):
        self.idade += 1

rex = Cachorro("Rex", 3)
print(rex.latir())       # Rex está latindo: Au au!
rex.aniversario()
print(rex.idade)         # 4
```

---

## 5. Encapsulamento

Controla o acesso direto aos atributos, protegendo o estado interno do objeto.

```python
class ContaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial       # convenção: "protegido" (uso interno)
        self.__senha = "1234"             # "privado" (name mangling)

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def consultar_saldo(self):
        return self._saldo

conta = ContaBancaria(100)
conta.depositar(50)
print(conta.consultar_saldo())  # 150

# print(conta.__senha)  # ERRO: AttributeError (name mangling)
print(conta._ContaBancaria__senha)  # ainda acessível, mas não é recomendado
```

**Convenções (Python não impõe privacidade real):**
- `atributo` → público
- `_atributo` → "protegido" (convenção: uso interno, mas acessível)
- `__atributo` → "privado" (name mangling dificulta acesso direto)

---

## 6. Herança

Permite que uma classe (filha) herde atributos e métodos de outra (mãe/base).

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def emitir_som(self):  # sobrescreve (override) o método da classe mãe
        return "Au au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

rex = Cachorro("Rex")
print(rex.nome)          # Rex (herdado de Animal)
print(rex.emitir_som())  # Au au!
```

Usando `super()` para chamar o método da classe mãe:

```python
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)  # chama o __init__ da classe mãe
        self.equipe = equipe

gerente = Gerente("Ana", 8000, ["Bruno", "Carla"])
print(gerente.nome, gerente.salario, gerente.equipe)
```

---

## 7. Polimorfismo

Objetos de classes diferentes respondendo ao mesmo método, cada um à sua maneira.

```python
animais = [Cachorro("Rex"), Gato("Miau")]

for animal in animais:
    print(animal.emitir_som())  # cada um chama sua própria versão
# Au au!
# Miau!
```

---

## 8. Métodos especiais (dunder methods)

Métodos com nome entre `__` (double underscore) que definem comportamentos especiais dos objetos.

```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Usado por print() e str() — versão legível para humanos."""
        return f"Ponto({self.x}, {self.y})"

    def __repr__(self):
        """Usado no console/debug — versão técnica."""
        return f"Ponto(x={self.x}, y={self.y})"

    def __eq__(self, outro):
        """Define o comportamento do operador ==."""
        return self.x == outro.x and self.y == outro.y

    def __add__(self, outro):
        """Define o comportamento do operador +."""
        return Ponto(self.x + outro.x, self.y + outro.y)

p1 = Ponto(1, 2)
p2 = Ponto(3, 4)

print(p1)              # Ponto(1, 2) — usa __str__
print(p1 == Ponto(1, 2))  # True — usa __eq__
print(p1 + p2)          # Ponto(4, 6) — usa __add__
```

---

## 9. Atributos e métodos de classe (static/classmethod)

```python
class Circulo:
    pi = 3.14159  # atributo de classe

    def __init__(self, raio):
        self.raio = raio

    def area(self):  # método de instância normal
        return Circulo.pi * self.raio ** 2

    @classmethod
    def a_partir_do_diametro(cls, diametro):
        """classmethod recebe a classe (cls), útil como construtor alternativo."""
        return cls(diametro / 2)

    @staticmethod
    def eh_positivo(numero):
        """staticmethod não recebe self nem cls — função utilitária dentro da classe."""
        return numero > 0

c1 = Circulo(5)
c2 = Circulo.a_partir_do_diametro(10)  # cria com raio 5
print(Circulo.eh_positivo(-3))  # False
```

---

## 10. Properties (getters/setters pythônicos)

Permitem controlar acesso a atributos com sintaxe de atributo comum, sem precisar de `get_x()`/`set_x()`.

```python
class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):
        """Getter — chamado quando se acessa produto.preco"""
        return self._preco

    @preco.setter
    def preco(self, novo_valor):
        """Setter — chamado quando se faz produto.preco = valor"""
        if novo_valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = novo_valor

produto = Produto(100)
print(produto.preco)   # 100 (chama o getter, sem parênteses!)
produto.preco = 150    # chama o setter
# produto.preco = -10  # ERRO: ValueError
```

---

## 11. Classes abstratas

Definem uma "interface" que classes filhas são obrigadas a implementar. Usa o módulo `abc`.

```python
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        """Toda forma precisa implementar esse método."""
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# forma = FormaGeometrica()  # ERRO: não pode instanciar classe abstrata
quadrado = Quadrado(4)
print(quadrado.area())  # 16
```

---

## 12. Composição vs Herança

- **Herança**: "é um" (`Cachorro` **é um** `Animal`)
- **Composição**: "tem um" (`Carro` **tem um** `Motor`)

```python
class Motor:
    def ligar(self):
        return "Motor ligado"

class Carro:
    def __init__(self):
        self.motor = Motor()  # composição: Carro TEM UM Motor

    def ligar(self):
        return self.motor.ligar()

carro = Carro()
print(carro.ligar())  # Motor ligado
```

> Regra geral: prefira composição quando a relação não é claramente "é um tipo de". Herança em excesso pode deixar o código rígido e difícil de manter.

---

## 13. Boas práticas

- Nomeie classes com `PascalCase` (`ContaBancaria`) e métodos/atributos com `snake_case`
- Use `__init__` para garantir que o objeto nasça em um estado válido
- Prefira composição a herança quando a relação não for clara
- Use `@property` para validar valores antes de aceitar mudanças
- Documente classes e métodos complexos com docstrings

---

## 14. Erros comuns

1. **Esquecer o `self`** como primeiro parâmetro dos métodos.
2. **Confundir atributo de classe com atributo de instância** — atributos de classe são compartilhados entre todas as instâncias.
```python
class Exemplo:
    lista = []  # CUIDADO: compartilhada entre todas as instâncias!

    def __init__(self):
        self.lista.append(1)  # afeta TODAS as instâncias
```
3. **Não usar `super().__init__()`** ao herdar, esquecendo de inicializar atributos da classe mãe.
4. **Abusar de herança múltipla** sem entender a ordem de resolução de métodos (MRO), gerando comportamento inesperado.

---

## Resumo rápido (cheat sheet)

```python
class MinhaClasse(ClasseMae):
    atributo_de_classe = valor

    def __init__(self, param):
        super().__init__()
        self.atributo = param

    def metodo(self):
        return self.atributo

    @classmethod
    def metodo_de_classe(cls):
        ...

    @staticmethod
    def metodo_estatico():
        ...

    @property
    def valor(self):
        return self._valor

    def __str__(self):
        return "representação em texto"
```
