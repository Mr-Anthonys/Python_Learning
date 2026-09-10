# Herança (POO)

## Explicação informal

Imagina que você já tem uma classe `Animal` com nome, idade e o método `fazer_som()`. Agora você quer criar `Cachorro` e `Gato`. Em vez de reescrever tudo do zero, você diz: "`Cachorro` é um tipo de `Animal`, então ele já nasce com tudo que `Animal` tem, e eu só adiciono ou modifico o que for específico do cachorro."

Isso é herança: uma classe "filha" (subclasse) herda atributos e métodos de uma classe "mãe" (superclasse), evitando repetir código.

## Explicação formal

Herança é o mecanismo da POO que permite que uma classe (subclasse/classe filha) **derive** de outra classe (superclasse/classe pai), herdando seus atributos e métodos, podendo também sobrescrevê-los (override) ou estendê-los.

### Sintaxe básica

```python
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("Som genérico de animal")

    def apresentar(self):
        print(f"{self.nome} tem {self.idade} anos")


class Cachorro(Animal):  # Cachorro herda de Animal
    def fazer_som(self):  # sobrescrevendo (override) o método da classe pai
        print("Au au!")


class Gato(Animal):
    def fazer_som(self):
        print("Miau!")


rex = Cachorro("Rex", 3)
rex.apresentar()   # herdado de Animal -> "Rex tem 3 anos"
rex.fazer_som()    # sobrescrito em Cachorro -> "Au au!"
```

### `super()` — chamando o método da classe pai

Quando você sobrescreve `__init__` (ou outro método) na subclasse, mas ainda quer aproveitar a lógica da classe pai, usa `super()`:

```python
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)  # reaproveita o __init__ de Animal
        self.raca = raca               # adiciona algo novo, específico de Cachorro

    def fazer_som(self):
        print("Au au!")


rex = Cachorro("Rex", 3, "Vira-lata")
print(rex.nome, rex.idade, rex.raca)  # Rex 3 Vira-lata
```

Sem `super().__init__(nome, idade)`, você teria que reescrever `self.nome = nome` e `self.idade = idade` manualmente dentro de `Cachorro`, duplicando código.

### Sobrescrita de método (override)

Quando a subclasse define um método com o **mesmo nome** de um método da superclasse, o método da subclasse "vence" — é o que será executado.

```python
class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

g = Gato("Mimi", 2)
g.fazer_som()  # Miau! (sobrescreve o "Som genérico de animal")
```

### `isinstance()` e `issubclass()`

```python
print(isinstance(rex, Cachorro))  # True
print(isinstance(rex, Animal))    # True -> Cachorro também É um Animal
print(issubclass(Cachorro, Animal))  # True
```

### Herança múltipla (Python permite)

```python
class Nadador:
    def nadar(self):
        print("Nadando...")

class Voador:
    def voar(self):
        print("Voando...")

class Pato(Animal, Nadador, Voador):
    pass

p = Pato("Donald", 1)
p.nadar()  # Nadando...
p.voar()   # Voando...
```

Python resolve qual método usar através do **MRO (Method Resolution Order)** quando há conflito de nomes entre as classes herdadas — pode ver com `Pato.__mro__`.

---

## Conteúdo bônus (extra — fora do escopo básico)

- **MRO (Method Resolution Order)**: a ordem em que Python busca métodos quando há herança múltipla. Pode inspecionar com `NomeDaClasse.__mro__` ou `NomeDaClasse.mro()`.
- **`__init_subclass__`**: hook chamado automaticamente sempre que uma classe é herdada — útil para registrar subclasses automaticamente.
- **Composição vs Herança**: nem sempre herança é a melhor escolha. Às vezes é melhor "ter um" (composição) do que "ser um" (herança). Ex: um `Carro` não deveria herdar de `Motor` — ele deveria **ter** um `Motor` como atributo.

```python
# Exemplo rápido de composição (alternativa à herança)
class Motor:
    def ligar(self):
        print("Motor ligado")

class Carro:
    def __init__(self):
        self.motor = Motor()  # Carro TEM um Motor, não É um Motor

    def ligar_carro(self):
        self.motor.ligar()  # delega a responsabilidade para o objeto Motor

c = Carro()
c.ligar_carro()  # Motor ligado
```
