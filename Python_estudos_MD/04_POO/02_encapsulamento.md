# Encapsulamento (POO)

## Explicação informal

Pensa num caixa eletrônico. Você não tem acesso direto ao dinheiro guardado no cofre do banco — você só interage através de botões e telas específicas (sacar, consultar saldo). O banco "esconde" o acesso direto ao cofre e só libera operações controladas.

Encapsulamento é isso: proteger os dados internos de um objeto, controlando como eles podem ser acessados ou modificados, ao invés de deixar qualquer parte do código mexer diretamente neles.

## Explicação formal

Encapsulamento é o pilar da POO que consiste em **restringir o acesso direto aos atributos de um objeto**, expondo apenas o necessário através de métodos controlados (getters/setters), protegendo a integridade dos dados.

### Níveis de "privacidade" em Python

Python não tem `private`/`public` como Java. Ele usa **convenção de nomes**:

| Convenção | Nome | Significado |
|---|---|---|
| `nome` | Público | Acesso livre, sem restrição |
| `_nome` | Protegido (convenção) | "Uso interno" — uma convenção, não é bloqueado de fato |
| `__nome` | Privado (name mangling) | Python renomeia internamente para dificultar acesso externo |

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular        # público
        self._agencia = "0001"        # protegido (convenção)
        self.__saldo = saldo          # privado (name mangling)

conta = ContaBancaria("Ana", 1000)
print(conta.titular)      # OK - Ana
print(conta._agencia)     # funciona, mas por convenção não deveria ser acessado de fora
print(conta.__saldo)      # AttributeError!
```

### Name mangling (o "privado" de Python)

Quando você usa `__saldo` (dois underscores), Python internamente renomeia o atributo para `_ContaBancaria__saldo`. Isso não é criptografia nem bloqueio real — é uma forma de **dificultar acesso acidental**, não impedir de propósito.

```python
print(conta._ContaBancaria__saldo)  # 1000 -> ainda é acessível, só "escondido"
```

### Getters e Setters — a forma tradicional

Getters e setters são métodos para **ler** e **alterar** um atributo privado de forma controlada:

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):          # getter
        return self.__saldo

    def set_saldo(self, valor):   # setter
        if valor < 0:
            print("Saldo não pode ser negativo!")
        else:
            self.__saldo = valor

conta = ContaBancaria("Ana", 1000)
print(conta.get_saldo())   # 1000
conta.set_saldo(-50)       # Saldo não pode ser negativo!
conta.set_saldo(1500)
print(conta.get_saldo())   # 1500
```

### `@property` — a forma "pythônica" de getter/setter

Em Python, o jeito mais idiomático de fazer getter/setter é com o decorator `@property`. Ele permite acessar um método **como se fosse um atributo comum** (sem parênteses), mantendo o controle por trás.

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        """Getter: chamado quando você faz conta.saldo"""
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        """Setter: chamado quando você faz conta.saldo = valor"""
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo!")
        self.__saldo = valor


conta = ContaBancaria("Ana", 1000)
print(conta.saldo)      # chama o getter -> 1000 (sem parênteses!)
conta.saldo = 2000      # chama o setter -> valida e atualiza
print(conta.saldo)      # 2000

conta.saldo = -100      # ValueError: Saldo não pode ser negativo!
```

**Vantagem do `@property`**: de fora, parece um atributo normal (`conta.saldo`), mas por dentro está passando por validação — sem que quem usa a classe precise saber disso.

### `@property` só de leitura (sem setter)

Se você só define `@property` e não define `.setter`, o atributo vira **somente leitura**:

```python
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def area(self):
        return 3.14159 * (self.raio ** 2)

c = Circulo(5)
print(c.area)   # 78.53975 -> calculado dinamicamente

c.area = 100    # AttributeError: can't set attribute (não existe setter)
```

---

## Conteúdo bônus (extra — fora do escopo básico)

- **`@nome.deleter`**: permite customizar o que acontece quando você faz `del objeto.atributo`.
- **`property()` como função** (forma antiga, antes dos decorators existirem) — bom saber que existe, mas hoje raramente usada.
- **Dataclasses (`@dataclass`)**: para classes que são "só dados", o Python oferece uma forma de gerar `__init__` automaticamente, reduzindo boilerplate de encapsulamento simples.

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("Preço deve ser positivo")
        self._preco = valor

    @preco.deleter
    def preco(self):
        print("Removendo preço...")
        del self._preco


p = Produto("Caneta", 2.50)
del p.preco   # Removendo preço...
```
