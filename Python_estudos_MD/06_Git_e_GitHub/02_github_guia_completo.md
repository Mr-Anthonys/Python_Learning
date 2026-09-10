# GitHub — Guia do Básico ao Avançado

## 1. O que é o GitHub

O **GitHub** é uma plataforma de hospedagem de repositórios Git na nuvem, com recursos de colaboração: Pull Requests, Issues, revisão de código, automação (Actions), páginas web estáticas (Pages) e muito mais.

**Git ≠ GitHub**: o Git é a ferramenta de controle de versão (funciona sem internet); o GitHub é um serviço que hospeda repositórios Git e adiciona colaboração social/empresarial em cima disso. Existem alternativas como GitLab e Bitbucket.

---

## 2. Autenticação

Desde 2021, o GitHub não aceita mais senha comum para operações via linha de comando — é preciso usar **token** ou **SSH**.

### Opção A: HTTPS + Personal Access Token (PAT)
1. GitHub → Settings → Developer settings → Personal access tokens → Generate new token
2. Ao fazer `git push`, use o token no lugar da senha

### Opção B: SSH (recomendado para uso frequente)
```bash
ssh-keygen -t ed25519 -C "seu@email.com"    # gera par de chaves
cat ~/.ssh/id_ed25519.pub                     # copia a chave pública
```
Cole a chave pública em GitHub → Settings → SSH and GPG keys → New SSH key.

Testar conexão:
```bash
ssh -T git@github.com
```

Clonar via SSH:
```bash
git clone git@github.com:usuario/repositorio.git
```

---

## 3. Criando e conectando um repositório

```bash
# Criar localmente e conectar a um repo já criado no GitHub
git init
git remote add origin git@github.com:usuario/repositorio.git
git branch -M main
git push -u origin main
```

Ou clone um já existente:
```bash
git clone git@github.com:usuario/repositorio.git
```

---

## 4. Fork vs Clone

| Conceito | O que é | Quando usar |
|---|---|---|
| **Clone** | Baixa uma cópia local de um repositório | Quando você já tem acesso de escrita (é dono ou colaborador) |
| **Fork** | Cria uma cópia do repositório na SUA conta do GitHub | Quando você quer contribuir com um projeto de outra pessoa/organização sem ter acesso direto |

Fluxo típico de contribuição open-source:
```
1. Fork do repositório original (no site do GitHub)
2. git clone do SEU fork
3. Criar uma branch para a alteração
4. Commitar e dar push no seu fork
5. Abrir um Pull Request do seu fork para o repositório original
```

---

## 5. Pull Requests (PR)

O **Pull Request** é o coração da colaboração no GitHub: uma proposta de mudança que outra pessoa revisa antes de aceitar (merge) no branch principal.

Fluxo básico:
```bash
git switch -c feature/nova-funcionalidade
# ... trabalha e comita ...
git push -u origin feature/nova-funcionalidade
```
Depois, no site do GitHub: **Compare & pull request** → descreve a mudança → solicita revisão.

Boas práticas de PR:
- Título claro e descritivo
- Descrição explicando o "porquê", não só o "o quê"
- PRs pequenos e focados são mais fáceis de revisar
- Vincular a Issue relacionada (ex.: `Closes #12`)
- Aguardar aprovação (review) antes do merge, especialmente em times

Tipos de merge de PR no GitHub:
| Tipo | Efeito |
|---|---|
| **Merge commit** | Preserva todos os commits + cria um commit de merge |
| **Squash and merge** | Junta todos os commits do PR em um único commit |
| **Rebase and merge** | Reaplica os commits do PR linearmente, sem commit de merge |

---

## 6. Issues

Usadas para reportar bugs, sugerir melhorias ou organizar tarefas.

- Podem receber **labels** (bug, enhancement, documentation...)
- Podem ser atribuídas a pessoas (**assignees**)
- Podem ser organizadas em **Milestones** (agrupamento por entrega/versão)
- Podem ser vinculadas a PRs: usar `Closes #número`, `Fixes #número` ou `Resolves #número` na descrição do PR fecha a issue automaticamente ao mergear

---

## 7. Code Review

Ao revisar um PR, é possível:
- Comentar linhas específicas do código
- Sugerir mudanças diretamente (**Suggest changes**), que o autor pode aceitar com um clique
- Aprovar, solicitar mudanças (**Request changes**) ou apenas comentar

Boas práticas como revisor:
- Foque em lógica, clareza e possíveis bugs, não apenas estilo
- Seja específico e construtivo nos comentários
- Separe "isso é obrigatório" de "isso é sugestão" (ex.: prefixo `nit:` para sugestões pequenas)

---

## 8. GitHub Actions (CI/CD)

Permite automatizar tarefas (testes, build, deploy) quando eventos acontecem no repositório (push, PR, etc).

Um workflow fica em `.github/workflows/nome.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Instalar dependências
        run: pip install -r requirements.txt
      - name: Rodar testes
        run: pytest
```

Conceitos:
| Termo | Significado |
|---|---|
| **Workflow** | Um processo automatizado completo (arquivo `.yml`) |
| **Job** | Um conjunto de passos que roda em uma máquina virtual |
| **Step** | Uma ação individual dentro de um job |
| **Action** | Uma unidade reutilizável de automação (própria ou da comunidade) |
| **Runner** | A máquina (VM) onde o workflow executa |

---

## 9. GitHub CLI (`gh`)

Ferramenta de linha de comando oficial do GitHub, permite interagir sem sair do terminal.

```bash
gh auth login                          # autentica
gh repo create nome-repo --public      # cria repositório
gh repo clone usuario/repo             # clona
gh pr create --title "Título" --body "Descrição"   # cria PR
gh pr list                             # lista PRs abertos
gh pr checkout 12                      # baixa localmente o PR #12
gh issue create                        # cria uma issue
gh issue list                          # lista issues
```

---

## 10. Outros recursos importantes

| Recurso | Função |
|---|---|
| **README.md** | Página inicial do repositório, primeira impressão do projeto |
| **GitHub Pages** | Hospeda sites estáticos direto de um repositório |
| **Branch protection rules** | Exige revisão, testes passando etc. antes de permitir merge na branch principal |
| **CODEOWNERS** | Define quem deve revisar automaticamente certas pastas/arquivos |
| **Discussions** | Espaço de fórum para debates, separado de Issues |
| **Projects** | Quadro estilo Kanban para organizar tarefas |
| **Secrets** | Variáveis sensíveis (tokens, senhas) usadas com segurança em Actions |
| **Dependabot** | Alerta e cria PRs automáticos para atualizar dependências vulneráveis |
| **GitHub Copilot** | Assistente de IA para sugestão de código dentro do editor |

---

## 11. Organizações e permissões

Repositórios podem pertencer a uma pessoa ou a uma **organização** (empresa/equipe).

Níveis de permissão comuns:
| Nível | Pode fazer |
|---|---|
| **Read** | Ver e clonar |
| **Triage** | Gerenciar issues/PRs sem acesso de escrita ao código |
| **Write** | Push direto (em repos onde permitido) e merge de PRs |
| **Maintain** | Gerenciar configurações do repositório, exceto sensíveis |
| **Admin** | Controle total, incluindo apagar o repositório |

---

## 12. Boas práticas gerais

- Nunca commitar credenciais, tokens ou chaves — usar `.gitignore` e **Secrets** do GitHub
- Escrever um bom README com instruções de instalação/uso
- Usar branch protection na `main` em projetos sérios (exigir PR + revisão)
- Adotar convenção de commits (ex.: [Conventional Commits](https://www.conventionalcommits.org)) para facilitar changelog automático
- Manter Issues e PRs organizados com labels e milestones

---

## 13. Próximos passos sugeridos

- Praticar o fluxo completo: fork → branch → PR → review → merge em um projeto pessoal
- Criar um workflow simples no GitHub Actions (ex.: rodar testes automaticamente)
- Explorar o `gh` CLI no dia a dia para agilizar tarefas
- Estudar branch protection rules e CODEOWNERS para simular um ambiente de equipe
