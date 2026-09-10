# Git e GitHub — Comandos Básicos

## Explicação informal

Git é uma ferramenta que guarda um "histórico de versões" do seu projeto — como um Ctrl+Z gigante, que registra cada mudança que você fez, quando fez, e permite voltar no tempo se precisar. GitHub é um site que hospeda esses projetos "na nuvem", permitindo compartilhar código e colaborar com outras pessoas.

Pense em Git como o "caderno de anotações local" do seu código, e GitHub como a "nuvem/backup compartilhado" desse caderno.

## Explicação formal

Git é um sistema de controle de versão distribuído que rastreia mudanças em arquivos ao longo do tempo. GitHub é uma plataforma de hospedagem de repositórios Git na nuvem, que adiciona funcionalidades de colaboração (Pull Requests, Issues, etc).

### `git init` — iniciar um repositório

Transforma uma pasta comum em um repositório Git (cria uma pasta oculta `.git/` que guarda todo o histórico):

```bash
git init
```

### `git clone` — copiar um repositório existente

Baixa uma cópia completa de um repositório remoto (do GitHub, por exemplo) para sua máquina, já com todo o histórico:

```bash
git clone https://github.com/usuario/nome-do-repositorio.git
```

### `git status` — ver o estado atual

Mostra quais arquivos foram modificados, quais estão "prontos" para commit, e quais ainda não estão sendo rastreados:

```bash
git status
```

### `git add` — preparar mudanças (staging)

Marca arquivos para serem incluídos no próximo commit:

```bash
git add nome_do_arquivo.py    # adiciona um arquivo específico
git add .                     # adiciona TODOS os arquivos modificados/novos
```

### `git commit` — salvar um "ponto" no histórico

Registra as mudanças marcadas com `git add` como um novo ponto no histórico, com uma mensagem explicando o que foi feito:

```bash
git commit -m "Adiciona função de validação de estoque"
```

> Boa prática: mensagens de commit devem ser curtas, no imperativo, e explicar **o que** mudou (ex: "Corrige bug de saldo negativo", não "mudei umas coisas").

### `git branch` — trabalhar com ramificações (branches)

Uma branch é uma "linha paralela" de desenvolvimento, isolada da branch principal (geralmente `main`), usada para desenvolver algo sem afetar o código estável:

```bash
git branch                       # lista as branches existentes
git branch nome-da-branch        # cria uma nova branch
git checkout nome-da-branch      # muda para essa branch
git checkout -b nome-da-branch   # cria E já muda para a nova branch (atalho)

# Sintaxe mais moderna (Git recente)
git switch nome-da-branch        # muda de branch
git switch -c nome-da-branch     # cria e muda de branch
```

### `git merge` — juntar branches

Incorpora as mudanças de uma branch dentro de outra (geralmente trazendo uma branch de funcionalidade de volta para a `main`):

```bash
git checkout main            # vai para a branch que vai RECEBER as mudanças
git merge nome-da-branch      # traz as mudanças de "nome-da-branch" para "main"
```

Se houver alterações conflitantes nos mesmos trechos de código, o Git aponta um **conflito de merge**, que precisa ser resolvido manualmente antes de continuar.

### `git pull` — trazer mudanças do repositório remoto

Baixa e já mescla as mudanças mais recentes do repositório remoto (GitHub) na sua branch local:

```bash
git pull origin main
```

`git pull` é, na prática, um `git fetch` (baixar mudanças) + `git merge` (mesclar) combinados.

### `git push` — enviar mudanças para o repositório remoto

Envia seus commits locais para o repositório remoto (GitHub), atualizando-o com seu histórico:

```bash
git push origin main
git push origin nome-da-branch    # enviando uma branch específica
```

### Pull Request (PR) — no GitHub, não no terminal

Depois de dar `push` em uma branch nova, você abre um **Pull Request** direto no site do GitHub: uma solicitação para que suas mudanças de uma branch sejam revisadas e depois mescladas (merged) na branch principal.

**Fluxo típico de trabalho com Pull Request:**

```bash
git checkout -b nova-funcionalidade   # 1. cria uma branch para a nova feature
# ... faz as alterações no código ...
git add .
git commit -m "Implementa nova funcionalidade X"
git push origin nova-funcionalidade   # 2. envia a branch para o GitHub
# 3. no site do GitHub, clica em "Compare & pull request"
# 4. depois de revisado (por você ou colegas), clica em "Merge pull request"
```

### Fluxo resumido (do dia a dia)

```bash
git status                          # ver o que mudou
git add .                           # preparar mudanças
git commit -m "mensagem clara"      # salvar no histórico local
git push origin nome-da-branch      # enviar para o GitHub
```

---

## Conteúdo bônus (extra — fora do escopo básico)

- **`.gitignore`**: arquivo que lista o que o Git deve **ignorar** (ex: `venv/`, `__pycache__/`, arquivos de configuração local com senhas).
- **`git log`**: mostra o histórico de commits — útil para entender o que já foi feito.
- **`git stash`**: "guarda de lado" temporariamente mudanças não commitadas, sem precisar fazer commit — útil quando você precisa trocar de branch rapidamente sem perder o trabalho em progresso.
- **`git rebase`**: alternativa ao `merge` para combinar histórico de forma mais "linear" (mais avançado, cuidado ao usar em branches compartilhadas).

```bash
# Exemplo de .gitignore comum em projetos Python
# venv/
# __pycache__/
# *.pyc
# .env

# Vendo o histórico de commits de forma resumida
git log --oneline

# Guardando mudanças temporariamente para trocar de branch
git stash            # guarda as mudanças não commitadas
git checkout outra-branch
# ... faz algo na outra branch ...
git checkout branch-original
git stash pop         # recupera as mudanças guardadas
```
