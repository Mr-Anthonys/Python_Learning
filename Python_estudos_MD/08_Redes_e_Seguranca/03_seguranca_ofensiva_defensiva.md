# Segurança Ofensiva e Defensiva — Guia do Básico ao Avançado

> ⚠️ **Aviso importante:** as técnicas descritas aqui devem ser aplicadas **apenas** em ambientes próprios, laboratórios controlados (ex.: TryHackMe, HackTheBox, VulnHub, DVWA) ou com autorização explícita por escrito do responsável pelo sistema (pentest contratado). Testar essas técnicas em sistemas de terceiros sem autorização é crime.

---

## 1. Conceitos fundamentais

| Termo | Significado |
|---|---|
| **Segurança Ofensiva** | Simula ataques para encontrar vulnerabilidades antes que atacantes reais o façam |
| **Segurança Defensiva** | Protege, detecta e responde a ataques (Blue Team) |
| **Red Team** | Time que ataca (simulação realista, muitas vezes sem avisar o Blue Team) |
| **Blue Team** | Time que defende e monitora |
| **Purple Team** | Combina Red + Blue para melhorar a defesa colaborativamente |
| **Pentest (teste de invasão)** | Processo estruturado e autorizado de encontrar e explorar vulnerabilidades |
| **Vulnerabilidade** | Falha que pode ser explorada |
| **Exploit** | Código/técnica que aproveita uma vulnerabilidade |
| **Payload** | O que o exploit executa (ex.: abrir um shell remoto) |
| **CVE** | Identificador padronizado de uma vulnerabilidade conhecida publicamente |

---

## 2. Tríade CIA (base de toda segurança)

| Princípio | Significado |
|---|---|
| **Confidencialidade** | Só quem deveria ter acesso, tem acesso |
| **Integridade** | Os dados não são alterados indevidamente |
| **Disponibilidade** | Sistemas continuam acessíveis quando necessário |

---

## 3. Metodologia de Pentest (visão ofensiva)

1. **Reconhecimento (Recon)** — coletar informações sobre o alvo
   - Passivo: OSINT, WHOIS, redes sociais, Google Dorking (sem interagir diretamente com o alvo)
   - Ativo: scans, enumeração (interage diretamente)
2. **Varredura (Scanning)** — mapear hosts, portas, serviços e versões
3. **Enumeração** — extrair detalhes específicos (usuários, compartilhamentos, versões de software)
4. **Exploração (Exploitation)** — explorar vulnerabilidades encontradas para obter acesso
5. **Pós-exploração** — escalar privilégios, manter persistência, mover lateralmente
6. **Relatório** — documentar tudo: vulnerabilidades, impacto, evidências, recomendações

---

## 4. Reconhecimento e OSINT

| Ferramenta/Técnica | Função |
|---|---|
| `whois <dominio>` | Informações de registro de domínio |
| Google Dorking | Buscas avançadas (`site:`, `filetype:`, `inurl:`) para achar dados expostos |
| `theHarvester` | Coleta e-mails, subdomínios e hosts de fontes públicas |
| Shodan | Motor de busca de dispositivos conectados à internet |
| `Sublist3r` / `amass` | Enumeração de subdomínios |

---

## 5. Varredura de rede (Scanning)

O **Nmap** é a ferramenta mais usada para mapear hosts, portas e serviços.

| Comando | Função |
|---|---|
| `nmap <alvo>` | Scan básico de portas comuns |
| `nmap -sV <alvo>` | Detecta versão dos serviços |
| `nmap -sС <alvo>` | Roda scripts padrão de detecção |
| `nmap -A <alvo>` | Scan agressivo (versão, SO, scripts, traceroute) |
| `nmap -p- <alvo>` | Escaneia todas as 65535 portas |
| `nmap -sS <alvo>` | Scan SYN (semi-aberto, mais furtivo) |
| `nmap -O <alvo>` | Detecta sistema operacional |
| `nmap -Pn <alvo>` | Ignora verificação de host ativo (ping) |

```bash
nmap -A -T4 -p- 192.168.1.10
```

---

## 6. Vulnerabilidades web mais comuns (OWASP Top 10)

| Vulnerabilidade | O que é |
|---|---|
| **Injection (SQLi, Command Injection)** | Entrada do usuário interpretada como código/comando |
| **Broken Authentication** | Falhas em login, sessão ou gestão de credenciais |
| **Sensitive Data Exposure** | Dados sensíveis expostos sem proteção adequada |
| **XML External Entities (XXE)** | Exploração de parsers XML mal configurados |
| **Broken Access Control** | Usuário acessa recursos que não deveria |
| **Security Misconfiguration** | Configurações padrão, permissões abertas, serviços desnecessários |
| **XSS (Cross-Site Scripting)** | Injeção de script malicioso em páginas visualizadas por outros usuários |
| **Insecure Deserialization** | Deserialização de dados não confiáveis |
| **Vulnerable Components** | Bibliotecas/dependências desatualizadas com falhas conhecidas |
| **Insufficient Logging & Monitoring** | Falta de registros para detectar e investigar incidentes |

### Exemplo simplificado de XSS
```html
<script>alert('XSS')</script>
```
Se um campo de comentário não sanitiza a entrada, esse código pode ser executado no navegador de outros usuários.

### Ferramentas para testes web
| Ferramenta | Função |
|---|---|
| **Burp Suite** | Intercepta e manipula requisições HTTP (essencial para pentest web) |
| **OWASP ZAP** | Alternativa gratuita/open-source ao Burp |
| **SQLmap** | Automatiza detecção e exploração de SQL Injection |
| **DVWA / Juice Shop** | Aplicações vulneráveis de propósito, para praticar legalmente |

---

## 7. Engenharia Social

Explora o fator humano, muitas vezes o elo mais fraco.

| Técnica | Descrição |
|---|---|
| **Phishing** | E-mails/mensagens falsas para roubar credenciais ou instalar malware |
| **Spear Phishing** | Phishing direcionado a uma pessoa/organização específica |
| **Pretexting** | Criar uma história falsa para obter informações |
| **Baiting** | Isca física ou digital (ex.: pendrive "esquecido") |
| **Vishing** | Phishing por voz/telefone |

---

## 8. Malware — visão geral

| Tipo | Descrição |
|---|---|
| **Vírus** | Se anexa a arquivos legítimos e se propaga quando executado |
| **Worm** | Se propaga sozinho pela rede, sem precisar de ação do usuário |
| **Trojan** | Se disfarça de programa legítimo |
| **Ransomware** | Criptografa dados e exige resgate |
| **Spyware** | Coleta informações sem o conhecimento do usuário |
| **Rootkit** | Se esconde profundamente no sistema para manter acesso persistente |

---

## 9. Escalação de privilégios (pós-exploração)

Depois de obter acesso inicial (geralmente limitado), o objetivo é conseguir mais privilégios.

| Linux | Windows |
|---|---|
| Verificar `sudo -l` (o que o usuário pode rodar como root) | Verificar serviços com permissões mal configuradas |
| Explorar SUID/SGID binaries mal configurados | Explorar tokens/privilégios (`whoami /priv`) |
| Kernel exploits desatualizados | DLL Hijacking |
| Cron jobs rodando como root com scripts editáveis | AlwaysInstallElevated / senhas em texto plano |

Ferramentas de enumeração automatizada: `LinPEAS` (Linux), `WinPEAS` (Windows).

---

## 10. Segurança Defensiva (Blue Team)

### Hardening (fortalecimento de sistemas)
- Desativar serviços/portas desnecessários
- Aplicar princípio do menor privilégio
- Manter sistemas e dependências atualizados (patch management)
- Usar autenticação multifator (MFA)
- Configurar firewalls corretamente (default deny)

### Monitoramento e detecção
| Ferramenta/Conceito | Função |
|---|---|
| **SIEM** (ex.: Splunk, ELK, Wazuh) | Centraliza e correlaciona logs para detectar anomalias |
| **IDS** (ex.: Snort, Suricata) | Detecta tráfego/atividade suspeita |
| **IPS** | Como o IDS, mas também bloqueia ativamente |
| **EDR** | Monitora e responde a ameaças em endpoints (estações/servidores) |
| **Honeypot** | Sistema-isca para atrair e estudar atacantes |

### Resposta a incidentes (Incident Response)
Fases comuns:
1. **Preparação** — políticas, ferramentas, treinamento
2. **Identificação** — detectar que algo aconteceu
3. **Contenção** — isolar o problema para não se espalhar
4. **Erradicação** — remover a causa raiz
5. **Recuperação** — restaurar sistemas com segurança
6. **Lições aprendidas** — documentar e melhorar processos

### Frameworks e referências importantes
| Framework | Uso |
|---|---|
| **MITRE ATT&CK** | Catálogo de táticas e técnicas usadas por atacantes reais |
| **NIST Cybersecurity Framework** | Diretrizes de gestão de risco cibernético |
| **OWASP** | Referência principal para segurança de aplicações web |
| **CIS Controls** | Lista priorizada de controles de segurança práticos |

---

## 11. Criptografia — noções essenciais

| Conceito | Descrição |
|---|---|
| **Criptografia simétrica** | Mesma chave para cifrar e decifrar (ex.: AES) — rápida |
| **Criptografia assimétrica** | Par de chaves pública/privada (ex.: RSA) — usada em HTTPS, SSH, assinatura digital |
| **Hash** | Transforma dados em um valor fixo, irreversível (ex.: SHA-256) — usado para senhas e integridade |
| **Salt** | Valor aleatório adicionado antes do hash de senhas, para evitar ataques de rainbow table |
| **HTTPS/TLS** | Combina simétrica + assimétrica para proteger tráfego web |

---

## 12. Senhas e ataques relacionados

| Ataque | Descrição |
|---|---|
| **Brute force** | Tenta todas as combinações possíveis |
| **Dictionary attack** | Testa senhas de uma lista (wordlist) conhecida |
| **Credential stuffing** | Reutiliza credenciais vazadas em outros serviços |
| **Rainbow table** | Tabela pré-computada de hashes para "descobrir" senhas rapidamente |

Ferramentas comuns (uso ético/laboratório): `Hydra`, `John the Ripper`, `Hashcat`.

---

## 13. Boas práticas gerais

- Sempre atuar com autorização formal (contrato/escopo definido) em pentests reais
- Documentar tudo durante um teste (evidências, comandos, horários)
- Aplicar defesa em profundidade (várias camadas de proteção, não uma só)
- Aplicar o princípio do menor privilégio em todos os acessos
- Treinar continuamente — segurança ofensiva e defensiva evoluem constantemente

---

## 14. Próximos passos sugeridos

- Praticar em plataformas legais como **TryHackMe** e **HackTheBox** (rooms para iniciantes)
- Montar um laboratório próprio com Kali Linux + DVWA/Metasploitable em VMs isoladas
- Explorar o **MITRE ATT&CK** navegador de técnicas
- Seguir para o arquivo de **Kali Linux**, que reúne as principais ferramentas ofensivas em um único sistema
- Depois, ver o arquivo de **Automação com Python**, que mostra como automatizar reconhecimento e exploração com sockets, Scapy, Requests e Paramiko
