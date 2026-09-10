# Git — Guia do Básico ao Avançado

## 1. O que é o Git

O **Git** é um sistema de controle de versão distribuído: ele registra o histórico de mudanças de um projeto, permite trabalhar em paralelo (branches), reverter erros e colaborar com outras pessoas sem sobrescrever o trabalho alheio.

Diferente de um backup simples, o Git guarda **snapshots** (fotografias) do estado dos arquivos a cada commit, não apenas as diferenças.

Instalação: [git-scm.com](https://git-scm.com). Verificar instalação:
```bash
git --version
```

---

## 2. Configuração inicial

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
git config --global core.editor "code --wait"   # define o VS Code como editor padrão
git config --list                                 # mostra todas as configurações
```

O `--global` aplica a config para todos os repositórios do usuário. Sem `--global`, vale só para o repositório atual.

---

## 3. Conceitos fundamentais

| Termo | Significado |
|---|---|
| **Repositório (repo)** | Pasta rastreada pelo Git, contém o histórico do projeto |
| **Working Directory** | Seus arquivos "reais", como você vê no explorador de arquivos |
| **Staging Area (Index)** | Área intermediária onde você prepara o que vai entrar no próximo commit |
| **Commit** | Um snapshot salvo do projeto, com uma mensagem descritiva |
| **Branch** | Uma linha de desenvolvimento independente |
| **HEAD** | Ponteiro para o commit/branch em que você está atualmente |
| **Remote** | Uma versão do repositório hospedada em outro lugar (ex.: GitHub) |

Fluxo básico:
```
Working Directory → (git add) → Staging Area → (git commit) → Repositório local → (git push) → Remoto
```

---

## 4. Criando e clonando repositórios

| Comando | Função |
|---|---|
| `git init` | Transforma a pasta atual em um repositório Git |
| `git clone <url>` | Copia um repositório remoto para a máquina local |
| `git clone <url> <pasta>` | Clona em uma pasta com nome customizado |

```bash
git init
git clone https://github.com/usuario/repositorio.git
```

---

## 5. Fluxo básico do dia a dia

| Comando | Função |
|---|---|
| `git status` | Mostra o estado atual (arquivos modificados, staged, etc.) |
| `git add <arquivo>` | Adiciona um arquivo à staging area |
| `git add .` | Adiciona todos os arquivos modificados/novos |
| `git commit -m "mensagem"` | Cria um commit com os arquivos em staging |
| `git commit -am "mensagem"` | Faz `add` + `commit` de arquivos já rastreados, em um passo |
| `git log` | Mostra o histórico de commits |
| `git log --oneline` | Histórico resumido, uma linha por commit |
| `git log --graph --oneline --all` | Histórico em formato de árvore (ótimo para visualizar branches) |
| `git diff` | Mostra diferenças não staged |
| `git diff --staged` | Mostra diferenças já staged, prontas para commit |

Boas práticas de mensagem de commit:
- Presente do indicativo: "Adiciona validação de login" (não "Adicionado")
- Curta e objetiva na primeira linha (até ~50 caracteres), detalhes no corpo se precisar

---

## 6. Branches (ramificações)

| Comando | Função |
|---|---|
| `git branch` | Lista as branches locais |
| `git branch <nome>` | Cria uma nova branch |
| `git switch <nome>` | Troca para outra branch (forma moderna) |
| `git checkout <nome>` | Troca para outra branch (forma clássica) |
| `git switch -c <nome>` | Cria e já muda para a nova branch |
| `git checkout -b <nome>` | Equivalente clássico do comando acima |
| `git branch -d <nome>` | Apaga uma branch (só se já estiver mesclada) |
| `git branch -D <nome>` | Força a exclusão de uma branch |
| `git branch -m <novo-nome>` | Renomeia a branch atual |

Fluxo típico:
```bash
git switch -c feature/login
# ... trabalha e comita ...
git switch main
git merge feature/login
```

---

## 7. Merge, rebase e conflitos

| Comando | Função |
|---|---|
| `git merge <branch>` | Junta o histórico de outra branch na atual |
| `git rebase <branch>` | Reaplica seus commits em cima de outra branch (histórico linear) |
| `git rebase -i <commit>` | Rebase interativo — reordenar, juntar (squash) ou editar commits |
| `git merge --abort` | Cancela um merge em andamento (em caso de conflito) |
| `git rebase --abort` | Cancela um rebase em andamento |

**Merge vs Rebase:**
- `merge` preserva o histórico real, criando um "commit de merge"
- `rebase` reescreve o histórico como se os commits tivessem sido feitos em sequência — mais "limpo", mas cuidado ao usar em branches compartilhadas com outras pessoas

Quando há **conflito** (o Git não sabe qual versão manter):
```bash
# o Git marca o arquivo com <<<<<<< ======= >>>>>>>
# edite manualmente escolhendo o que ficar
git add arquivo-resolvido.txt
git commit        # se for merge
git rebase --continue   # se for rebase
```

---

## 8. Trabalhando com remotos

| Comando | Função |
|---|---|
| `git remote -v` | Lista os remotos configurados |
| `git remote add origin <url>` | Adiciona um remoto chamado "origin" |
| `git push origin <branch>` | Envia commits locais para o remoto |
| `git push -u origin <branch>` | Envia e já associa a branch local à remota (próximos `push` não precisam do nome) |
| `git pull` | Busca e já mescla mudanças do remoto (`fetch` + `merge`) |
| `git pull --rebase` | Busca mudanças e reaplica seus commits por cima (evita commit de merge) |
| `git fetch` | Busca mudanças do remoto sem mesclar automaticamente |

---

## 9. Desfazendo mudanças

| Comando | Função | Nível de "perigo" |
|---|---|---|
| `git restore <arquivo>` | Descarta mudanças não staged de um arquivo | Cuidado — perde alterações |
| `git restore --staged <arquivo>` | Remove um arquivo da staging area (sem apagar mudanças) | Seguro |
| `git checkout -- <arquivo>` | Forma antiga de descartar mudanças (equivalente ao restore) | Cuidado |
| `git reset <arquivo>` | Remove um arquivo do staging | Seguro |
| `git reset --soft HEAD~1` | Desfaz o último commit, mantendo mudanças staged | Seguro |
| `git reset --mixed HEAD~1` | Desfaz commit e staging, mantém mudanças no working dir (padrão) | Moderado |
| `git reset --hard HEAD~1` | Desfaz commit e apaga TODAS as mudanças | ⚠️ Perigoso — perde trabalho |
| `git revert <hash>` | Cria um novo commit que desfaz um commit anterior (seguro para histórico compartilhado) | Seguro |

**Regra prática:** use `revert` em branches compartilhadas (não reescreve histórico), e `reset` só em commits locais que ainda não foram enviados (`push`).

---

## 10. Stash (guardar mudanças temporariamente)

Útil quando você precisa trocar de branch mas ainda não quer commitar o que está fazendo.

| Comando | Função |
|---|---|
| `git stash` | Guarda as mudanças atuais e limpa o working directory |
| `git stash list` | Lista os stashes salvos |
| `git stash pop` | Aplica o último stash e o remove da lista |
| `git stash apply` | Aplica o último stash, mas mantém na lista |
| `git stash drop` | Remove um stash sem aplicá-lo |
| `git stash -u` | Inclui arquivos não rastreados (untracked) no stash |

---

## 11. Tags

Usadas para marcar pontos importantes, como versões de release.

```bash
git tag v1.0.0                          # tag simples
git tag -a v1.0.0 -m "Primeira versão"  # tag anotada (com mensagem)
git push origin v1.0.0                  # envia uma tag específica
git push origin --tags                  # envia todas as tags
git tag -d v1.0.0                       # apaga tag localmente
```

---

## 12. .gitignore

Arquivo que define o que o Git deve ignorar (não rastrear).

```gitignore
# Exemplo de .gitignore para Python
__pycache__/
*.pyc
.venv/
.env
*.log
.DS_Store
```

Se um arquivo já estava sendo rastreado antes de entrar no `.gitignore`, é preciso removê-lo do rastreamento:
```bash
git rm --cached arquivo.txt
```

---

## 13. Investigando o histórico (avançado)

| Comando | Função |
|---|---|
| `git show <hash>` | Mostra detalhes de um commit específico |
| `git blame <arquivo>` | Mostra quem alterou cada linha de um arquivo, e em qual commit |
| `git bisect` | Busca binária no histórico para encontrar o commit que introduziu um bug |
| `git reflog` | Mostra o histórico de tudo que o HEAD já apontou (ótimo para "recuperar" commits perdidos) |
| `git cherry-pick <hash>` | Aplica um commit específico de outra branch na branch atual |

Exemplo de recuperação com `reflog`:
```bash
git reflog                  # encontra o hash do commit "perdido"
git checkout <hash>         # ou git reset --hard <hash>
```

---

## 14. Boas práticas

- Faça commits pequenos e frequentes, cada um com uma responsabilidade clara
- Nunca faça `reset --hard` ou `push --force` em branches compartilhadas sem ter certeza
- Use branches para cada feature/bugfix (`feature/`, `fix/`, `hotfix/`)
- Escreva um `.gitignore` desde o início do projeto
- Prefira `git pull --rebase` para manter o histórico mais limpo em times pequenos
- Revise com `git diff` antes de commitar

---

## 15. Próximos passos sugeridos

- Praticar resolução de conflitos de merge propositalmente
- Aprender `git rebase -i` para organizar commits antes de um push
- Estudar Git Flow / Trunk-Based Development como estratégias de branching
- Seguir para o arquivo de **GitHub**, que cobre Pull Requests, Issues, Actions e fluxo colaborativo
