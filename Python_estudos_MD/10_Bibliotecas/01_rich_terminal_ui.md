# Rich (Python) — Do Básico ao Avançado

Biblioteca para deixar a saída do terminal bonita: cores, tabelas, barras de progresso, painéis, markdown, syntax highlighting, tracebacks legíveis e muito mais.

```bash
pip install rich
```

Teste rápido pra ver do que ela é capaz (roda uma demo completa no terminal):

```bash
python -m rich
```

---

## 1. Console básico

Tudo gira em torno do objeto `Console`. Ele substitui o `print()` comum.

```python
from rich.console import Console

console = Console()

console.print("Olá, mundo!")
console.print("Isso é [bold red]vermelho e negrito[/bold red]")
console.print("Isso é [italic cyan]itálico ciano[/italic cyan]")
```

A sintaxe `[estilo]texto[/estilo]` é o **markup** do Rich — parecido com BBCode.

---

## 2. Cores e estilos (markup)

### Estilos combináveis
```python
console.print("[bold]negrito[/bold]")
console.print("[italic]itálico[/italic]")
console.print("[underline]sublinhado[/underline]")
console.print("[strike]riscado[/strike]")
console.print("[dim]esmaecido[/dim]")
console.print("[blink]piscando[/blink]")
console.print("[reverse]invertido (fundo/texto trocados)[/reverse]")
```

### Cores de texto e fundo
```python
console.print("[red]texto vermelho[/red]")
console.print("[white on blue]texto branco fundo azul[/white on blue]")
console.print("[bold magenta on black]combo completo[/bold magenta on black]")
```

### Cores por código (hex ou número 0-255)
```python
console.print("[#ff8800]cor hexadecimal[/#ff8800]")
console.print("[color(202)]cor por número (paleta 256)[/color(202)]")
```

**Comando útil** — mostra a tabela com todas as cores nomeadas e seus códigos:
```bash
python -m rich.color
```

### Objeto Style (alternativa ao markup)
```python
from rich.style import Style

estilo_alerta = Style(color="yellow", bold=True, underline=True)
console.print("Atenção!", style=estilo_alerta)
```

### Estilos combinados por variável (reutilizar)
```python
console.print("Erro crítico", style="bold white on red")
console.print("Sucesso", style="bold green")
console.print("Aviso", style="bold yellow")
```

---

## 3. `print()` com argumentos especiais

```python
console.print("Item", "valor", sep=" -> ")
console.print("Centralizado", justify="center")
console.print("Texto que não quebra linha", no_wrap=True)
console.print("x" * 200)  # quebra automática respeitando a largura do terminal
```

### `rprint` — atalho global (sem precisar criar Console)
```python
from rich import print as rprint

rprint("[bold blue]Atalho rápido[/bold blue]")
```

---

## 4. Emojis

Rich converte `:nome_do_emoji:` automaticamente.

```python
console.print(":thumbs_up: Deu certo!")
console.print(":warning: Cuidado com isso")
console.print(":rocket: Deploy feito :tada:")
```

**Comando útil** — lista TODOS os nomes de emoji suportados (ótimo pra descobrir o nome certo):
```bash
python -m rich.emoji
```

---

## 5. Tabelas

```python
from rich.table import Table

tabela = Table(title="Usuários")

tabela.add_column("Nome", style="cyan", no_wrap=True)
tabela.add_column("Idade", justify="right", style="magenta")
tabela.add_column("Cidade", style="green")

tabela.add_row("Ana", "28", "São Paulo")
tabela.add_row("Bruno", "35", "Rio de Janeiro")
tabela.add_row("Carla", "22", "Belo Horizonte")

console.print(tabela)
```

### Opções úteis de tabela
```python
tabela = Table(
    title="Relatório",
    show_lines=True,        # linhas divisórias entre cada linha
    header_style="bold white on blue",
    border_style="bright_black",
    caption="Atualizado hoje",
)
```

**Comando útil** — vê um exemplo de tabela pronta rodando:
```bash
python -m rich.table
```

---

## 6. Painéis (Panel)

Coloca uma borda ao redor de qualquer conteúdo.

```python
from rich.panel import Panel

console.print(Panel("Conteúdo importante", title="Aviso", border_style="red"))
console.print(Panel.fit("Ajusta ao tamanho do texto"))
```

---

## 7. Colunas (Columns)

Organiza vários itens lado a lado automaticamente.

```python
from rich.columns import Columns

itens = [f"Item {i}" for i in range(20)]
console.print(Columns(itens))
```

---

## 8. Barra de progresso (Progress)

```python
from rich.progress import Progress
import time

with Progress() as progress:
    tarefa = progress.add_task("[cyan]Processando...", total=100)
    while not progress.finished:
        progress.update(tarefa, advance=5)
        time.sleep(0.1)
```

### Múltiplas barras simultâneas
```python
with Progress() as progress:
    t1 = progress.add_task("[red]Download", total=100)
    t2 = progress.add_task("[green]Processamento", total=100)
    t3 = progress.add_task("[cyan]Upload", total=100)

    while not progress.finished:
        progress.update(t1, advance=1.5)
        progress.update(t2, advance=1.0)
        progress.update(t3, advance=0.8)
        time.sleep(0.05)
```

### Forma simplificada, sem `with` (iterando uma lista)
```python
from rich.progress import track

for item in track(range(20), description="Trabalhando..."):
    time.sleep(0.1)
```

---

## 9. Spinner / status (tarefas sem progresso definido)

```python
import time

with console.status("[bold green]Carregando dados...") as status:
    time.sleep(3)
    console.log("Dados carregados!")
```

---

## 10. Logging bonito

Substitui o `logging` padrão do Python por uma versão com cores e caminho do arquivo/linha.

```python
import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    handlers=[RichHandler()]
)

log = logging.getLogger("meu_app")
log.info("Aplicação iniciada")
log.warning("Isso é um aviso")
log.error("Isso é um erro")
```

---

## 11. Tracebacks (erros) legíveis

Substitui o traceback feio padrão do Python por um com cores, syntax highlighting e destaque da linha que quebrou.

```python
from rich.traceback import install
install()

# a partir daqui, qualquer erro não tratado vai aparecer formatado
1 / 0
```

Também funciona instalando globalmente logo no início do script principal — recomendado colocar isso no topo de qualquer projeto que você esteja depurando.

---

## 12. Syntax highlighting (mostrar código)

```python
from rich.syntax import Syntax

codigo = '''
def soma(a, b):
    return a + b
'''

syntax = Syntax(codigo, "python", theme="monokai", line_numbers=True)
console.print(syntax)
```

**Comando útil** — mostra um exemplo funcionando:
```bash
python -m rich.syntax
```

---

## 13. Renderizar Markdown no terminal

```python
from rich.markdown import Markdown

md = Markdown("# Título\n\nTexto **negrito** e *itálico*.\n\n- item 1\n- item 2")
console.print(md)
```

---

## 14. Árvore (Tree) — estrutura hierárquica

```python
from rich.tree import Tree

arvore = Tree("Projeto")
src = arvore.add("src")
src.add("main.py")
src.add("utils.py")
testes = arvore.add("tests")
testes.add("test_main.py")

console.print(arvore)
```

---

## 15. Layout (dividir o terminal em regiões)

```python
from rich.layout import Layout

layout = Layout()
layout.split_column(
    Layout(name="topo"),
    Layout(name="rodape"),
)
layout["topo"].update(Panel("Cabeçalho"))
layout["rodape"].update(Panel("Rodapé"))

console.print(layout)
```

---

## 16. Live (atualização em tempo real)

Útil para dashboards que atualizam sozinhos.

```python
from rich.live import Live
import time

with Live(refresh_per_second=4) as live:
    for i in range(20):
        live.update(Panel(f"Contagem: {i}"))
        time.sleep(0.25)
```

---

## 17. Prompt — pedir entrada do usuário com validação

```python
from rich.prompt import Prompt, Confirm, IntPrompt

nome = Prompt.ask("Qual seu nome?")
idade = IntPrompt.ask("Qual sua idade?")
confirma = Confirm.ask("Deseja continuar?")
```

---

## 18. `inspect` — debug rápido de qualquer objeto

Mostra métodos, atributos e docstring de forma organizada. Excelente para explorar bibliotecas desconhecidas direto no terminal.

```python
from rich import inspect

inspect(console, methods=True)
inspect([1, 2, 3])
```

---

## 19. Rich + `print` global (substituir o print padrão do projeto todo)

```python
from rich import print
# a partir daqui, todo print() do arquivo já ganha suporte a markup e cores
print("[bold green]Isso já funciona automaticamente[/bold green]")
```

---

## 20. Comandos de terminal úteis (colas rápidas)

Vários módulos do Rich têm uma demonstração embutida — rodar `python -m rich.<módulo>` mostra exemplos reais direto no terminal, sem precisar escrever código:

```bash
python -m rich              # demo geral com tudo (cores, tabelas, markdown, etc.)
python -m rich.color        # tabela com todas as cores nomeadas e seus códigos
python -m rich.emoji        # lista completa de nomes de emoji suportados
python -m rich.table        # exemplo de tabela pronta
python -m rich.syntax       # exemplo de syntax highlighting
python -m rich.markdown     # exemplo de renderização de markdown
python -m rich.progress     # exemplo de barra de progresso
python -m rich.panel        # exemplo de painel
python -m rich.tree         # exemplo de árvore
```

---

## 21. Cola prática — cheatsheet do dia a dia

```python
from rich.console import Console
console = Console()

# Mensagens de status (padrão útil pra scripts e automações)
console.print("[bold green]✔ Sucesso[/bold green]")
console.print("[bold yellow]⚠ Aviso[/bold yellow]")
console.print("[bold red]✘ Erro[/bold red]")
console.print("[bold cyan]ℹ Info[/bold cyan]")

# Log com timestamp automático
console.log("Isso aparece com hora, arquivo e linha")

# Print de qualquer objeto Python formatado (dict, list, etc.)
console.print({"chave": "valor", "numero": 42})

# Regra horizontal (separador visual)
console.rule("[bold blue]Seção nova")

# Texto justificado e com largura de terminal
console.print("Texto centralizado", justify="center")
```

### Tabela de referência rápida de estilos
| Markup | Efeito |
|---|---|
| `[bold]` | negrito |
| `[italic]` | itálico |
| `[underline]` | sublinhado |
| `[strike]` | riscado |
| `[dim]` | esmaecido |
| `[reverse]` | inverte cor do texto/fundo |
| `[red]`, `[green]`, `[blue]`... | cor do texto |
| `[on red]` | cor de fundo |
| `[#rrggbb]` | cor hexadecimal |
| `[color(N)]` | cor pela paleta 0-255 |

---

## 22. Próximos passos sugeridos

- Combinar `Live` + `Layout` + `Table` para montar um dashboard de terminal em tempo real.
- Usar `RichHandler` em projetos reais no lugar do `logging` padrão.
- Usar `install()` do `rich.traceback` em todo projeto novo — economiza muito tempo de debug.
- Explorar a documentação oficial: https://rich.readthedocs.io
