# Polimorfismo (POO)

## Explicação informal

"Poli" = muitas, "morfismo" = formas. Polimorfismo é a ideia de que **o mesmo comando pode se comportar de forma diferente dependendo do objeto que o recebe**.

Exemplo do dia a dia: o comando "toca!" significa uma coisa diferente para um violão, para um piano e para uma bateria — cada um "sabe" tocar do seu próprio jeito, mas você usa a mesma palavra de comando para todos.

## Explicação formal

Polimorfismo é o pilar da POO que permite que **objetos de classes diferentes respondam de forma diferente ao mesmo método/interface**, ou seja, um mesmo nome de método pode ter comportamentos distintos dependendo da classe do objeto que o executa.

### Polimorfismo via herança e sobrescrita (override)

Essa é a forma mais comum vista em conjunto com herança: várias subclasses implementam o mesmo método de formas diferentes.

```python
class Animal:
    def fazer_som(self):
        raise NotImplementedError

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

class Pato(Animal):
    def fazer_som(self):
        return "Quack!"


animais = [Cachorro(), Gato(), Pato()]

for animal in animais:
    print(animal.fazer_som())
# Au au!
# Miau!
# Quack!
```

Repare: o código do `for` **não sabe e não precisa saber** qual classe específica está processando. Ele só chama `.fazer_som()` e cada objeto responde do seu próprio jeito. Isso é polimorfismo em ação.

### Duck Typing — o polimorfismo "estilo Python"

Python é uma linguagem de tipagem dinâmica, então o polimorfismo não exige necessariamente herança de uma classe comum. Se o objeto "tem o método esperado", ele funciona — não importa a classe.

> "Se anda como um pato e faz quack como um pato, então é um pato" (duck typing)

```python
class Pato:
    def fazer_som(self):
        return "Quack!"

class Pessoa:
    def fazer_som(self):
        return "Estou imitando um pato: quack!"

# Pato e Pessoa NÃO têm relação de herança nenhuma entre si
for coisa in [Pato(), Pessoa()]:
    print(coisa.fazer_som())
# Quack!
# Estou imitando um pato: quack!
```

Isso funciona porque Python não verifica o **tipo** do objeto antes de chamar `.fazer_som()` — ele só verifica se o método existe.

### Polimorfismo com funções internas do Python (sobrecarga de operadores)

Você já viu polimorfismo sem perceber: `len()`, `+`, `str()` se comportam diferente dependendo do tipo:

```python
print(len("Python"))       # 6 (tamanho da string)
print(len([1, 2, 3]))      # 3 (tamanho da lista)
print(len({"a": 1, "b": 2}))  # 2 (quantidade de chaves)

print(1 + 2)        # 3 (soma numérica)
print("a" + "b")    # "ab" (concatenação)
print([1] + [2])    # [1, 2] (concatenação de listas)
```

Você pode fazer suas próprias classes se comportarem assim, sobrescrevendo métodos especiais (dunder methods) como `__add__`, `__len__`, `__str__`:

```python
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):   # sobrescreve o comportamento do operador +
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __str__(self):          # sobrescreve o que print() mostra
        return f"Vetor({self.x}, {self.y})"


v1 = Vetor(1, 2)
v2 = Vetor(3, 4)
v3 = v1 + v2         # chama __add__ internamente
print(v3)            # Vetor(4, 6) -> chama __str__ internamente
```

---

## Conteúdo bônus (extra — fora do escopo básico)

- **Sobrecarga de operadores completa**: além de `__add__`, existem `__sub__` (`-`), `__mul__` (`*`), `__eq__` (`==`), `__lt__` (`<`), entre outros — todos permitem polimorfismo customizado.
- **`typing.Protocol`**: forma moderna e tipada de expressar "duck typing" com checagem estática (mypy), sem exigir herança.
- **Polimorfismo paramétrico** (genéricos): usando `TypeVar` e `Generic` do módulo `typing`, para escrever código que funciona com múltiplos tipos mantendo tipagem estática.

```python
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __eq__(self, outro):
        # permite usar == entre dois objetos Retangulo comparando a área
        return (self.base * self.altura) == (outro.base * outro.altura)


r1 = Retangulo(2, 6)   # área 12
r2 = Retangulo(3, 4)   # área 12
print(r1 == r2)  # True -> comportamento customizado do operador ==
```
