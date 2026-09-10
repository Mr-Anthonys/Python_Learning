# Abstração (POO)

## Explicação informal

Pensa assim: quando você dirige um carro, você usa o volante, o pedal de freio e o acelerador. Você não precisa saber como o motor de combustão funciona por dentro, quais peças se mexem, como a injeção eletrônica calcula a mistura de ar e combustível. Você só precisa saber **o que** cada comando faz, não **como** ele faz por dentro.

Abstração em programação é exatamente isso: esconder a complexidade interna e mostrar só o que é necessário para quem vai usar a classe. Você cria uma "interface simples" (métodos com nomes claros) e esconde os detalhes de implementação.

## Explicação formal

Abstração é o pilar da POO que consiste em **modelar entidades do mundo real (ou do problema) representando apenas os atributos e comportamentos relevantes para o contexto**, ocultando detalhes de implementação desnecessários para quem consome a classe.

Em Python, a abstração é geralmente implementada com:

1. **Classes Abstratas** — usando o módulo `abc` (Abstract Base Classes), que impede a instanciação direta da classe e obriga as subclasses a implementarem certos métodos.
2. **Métodos abstratos** — métodos declarados na classe base mas sem implementação, que **devem** ser implementados nas subclasses.

### Sintaxe básica

```python
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass
```

- `ABC` (Abstract Base Class) é a classe da qual você herda para criar uma classe abstrata.
- `@abstractmethod` marca um método que **não tem implementação** na classe base e que é **obrigatório** implementar nas subclasses.

### Implementando as subclasses

```python
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14159 * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14159 * self.raio
```

### O que acontece se você não implementar um método abstrato?

```python
class Triangulo(FormaGeometrica):
    def calcular_area(self):
        return "área do triângulo"
    # esqueceu de implementar calcular_perimetro

t = Triangulo()
# TypeError: Can't instantiate abstract class Triangulo with abstract method calcular_perimetro
```

Python **impede a instanciação** de qualquer subclasse que não implemente todos os métodos abstratos da classe base. Isso é o Python garantindo que o "contrato" definido pela abstração seja cumprido.

### Por que isso é útil?

- Você garante que toda forma geométrica no seu sistema **vai ter** `calcular_area()` e `calcular_perimetro()`, sem se preocupar com a implementação de cada uma.
- Quem usa a classe `FormaGeometrica` (ou suas subclasses) não precisa saber a fórmula matemática por trás — só chama `.calcular_area()` e recebe o resultado.
- Facilita testes e manutenção, porque o "contrato" (interface) fica bem definido.

### Classe abstrata não pode ser instanciada diretamente

```python
forma = FormaGeometrica()
# TypeError: Can't instantiate abstract class FormaGeometrica with abstract methods calcular_area, calcular_perimetro
```

Isso é proposital: uma forma geométrica "genérica" não faz sentido sozinha — só faz sentido através de uma implementação concreta (`Retangulo`, `Circulo`, etc).

---

## Conteúdo bônus (extra — fora do escopo básico)

Coisas para explorar depois, quando abstração já estiver mais natural:

- **Métodos abstratos com implementação parcial**: um método abstrato pode ter um corpo, e as subclasses podem chamar `super().metodo()` para reaproveitar essa lógica.
- **`abstractproperty`** (hoje descontinuado — usa-se `@property` + `@abstractmethod` combinados) para forçar que subclasses implementem uma propriedade.
- **Protocolos (`typing.Protocol`)**: uma forma "estrutural" de abstração no Python moderno (duck typing tipado), sem precisar de herança.

```python
from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        ...

    def enviar_com_log(self, mensagem: str) -> None:
        # método concreto que usa o abstrato -> reaproveitamento de lógica
        print(f"[LOG] Preparando envio: {mensagem}")
        self.enviar(mensagem)  # delega para a implementação da subclasse


class NotificadorEmail(Notificador):
    def enviar(self, mensagem: str) -> None:
        print(f"E-mail enviado: {mensagem}")


n = NotificadorEmail()
n.enviar_com_log("Olá!")
# [LOG] Preparando envio: Olá!
# E-mail enviado: Olá!
```
