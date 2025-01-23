# python-week-one
 # Exercícios

## Exercício 1: Criar um Scanner de Rede Básico
**Descrição:** Desenvolva um programa que aceita uma lista de IPs e portas e verifica quais portas estão abertas.  
**Habilidades Praticadas:** Uso de loops, manipulação de listas, funções e exceções.  
**Tarefa:**
- Crie uma função que simula o teste de conexão a uma porta usando um `try/except`.
- Use `for` para iterar sobre os IPs e portas fornecidos.
- Retorne quais portas estão abertas para cada IP.

---

## Exercício 2: Criar um Módulo de Vulnerabilidades
**Descrição:** Crie um módulo chamado `vulnerabilidades.py` que contenha funções para cada tipo de vulnerabilidade.  
**Habilidades Praticadas:** Funções, módulos, dicionários e tratamento de exceções.  
**Tarefa:**
- Crie funções que simulam a verificação de cada vulnerabilidade (ex: `verifica_dns_recursion`, `verifica_ntp_ddos`, etc.).
- Cada função deve retornar `True` se a vulnerabilidade estiver presente e `False` caso contrário.
- Use dicionários para mapear vulnerabilidades às suas descrições e portas associadas.

---

## Exercício 3: Analisador de Logs de Conexões
**Descrição:** Desenvolva um programa que analisa logs de conexões de rede e identifica possíveis vulnerabilidades.  
**Habilidades Praticadas:** Manipulação de strings, listas, dicionários e funções.  
**Tarefa:**
- Crie uma função que lê um arquivo de log (simulado como uma lista de strings).
- Identifique conexões suspeitas com base em portas conhecidas associadas às vulnerabilidades.
- Retorne um relatório com IPs suspeitos e as vulnerabilidades possíveis.

**Exemplo de Log:**
```python
logs = [
    "192.168.1.1:53 - Conexão bem-sucedida",
    "192.168.1.2:123 - Conexão falhou",
    "192.168.1.3:445 - Conexão bem-sucedida"
]
```

**Saída Esperada:**
```plaintext
IP 192.168.1.1: Possível vulnerabilidade - DNS Recursion (Porta 53)
IP 192.168.1.3: Possível vulnerabilidade - Samba Outdated Version (Porta 445)
```

---

## Exercício 4: Gerenciador de Vulnerabilidades com Classes
**Descrição:** Desenvolva um sistema de gerenciamento de vulnerabilidades usando classes em Python.  
**Habilidades Praticadas:** Programação orientada a objetos (POO), classes, métodos e dicionários.  
**Tarefa:**
- Crie uma classe `Vulnerabilidade` com atributos como `nome`, `descricao`, `porta` e `status`.
- Adicione métodos para verificar se a vulnerabilidade está ativa e para gerar um relatório.
- Crie uma classe `GerenciadorVulnerabilidades` que armazena e gerencia uma lista de objetos `Vulnerabilidade`.

**Exemplo de Uso:**
```python
vuln1 = Vulnerabilidade("DNS Recursion", "Permite consultas de qualquer origem", 53)
vuln2 = Vulnerabilidade("NTP DDOS", "Amplificação de ataques DDoS", 123)

gerenciador = GerenciadorVulnerabilidades()
gerenciador.adicionar_vulnerabilidade(vuln1)
gerenciador.adicionar_vulnerabilidade(vuln2)

print(gerenciador.gerar_relatorio())
```

**Saída Esperada:**
```plaintext
Vulnerabilidades:
- DNS Recursion (Porta 53): Ativa
- NTP DDOS (Porta 123): Inativa
```

## Instruções Iniciais

### 1. **Criar um Repositório com Base no Template**
1. Acesse o repositório template: [template-week-one](https://github.com/GT-SIVT/template-week-one).
2. Clique no botão **"Use this template"** (Usar este modelo) no topo da página.
3. Na página de criação do repositório:
   - Escolha a organização **GT-SIVT** como proprietária.
   - Nomeie o repositório como `seunome-week-one` (substitua `seunome` pelo seu nome ou apelido).
   - Defina o repositório como **público**.
4. Clique em **"Create repository"** para finalizar.

---

### 2. **Clonar o Repositório**
1. Após criar o repositório, clone-o para sua máquina local:
   ```bash
   git clone https://github.com/GT-SIVT/seunome-week-one.git
   ```
2. Navegue até a pasta do repositório:
   ```bash
   cd seunome-week-one
   ```

---

### 3. **Trabalhar com Branches**
Sempre que for implementar uma nova funcionalidade ou resolver uma issue, crie uma branch específica. Isso ajuda a manter o código organizado e facilita a revisão.

1. Crie uma nova branch:
   ```bash
   git checkout -b feature/nome-da-feature
   ```
   Exemplo:
   ```bash
   git checkout -b feature/dns-recursion-check
   ```

2. Faça as alterações necessárias no código.

3. Adicione as mudanças ao staging area e faça um commit:
   ```bash
   git add .
   git commit -m "Descrição das alterações"
   ```

4. Envie a branch para o repositório remoto:
   ```bash
   git push origin feature/nome-da-feature
   ```

---

### 4. **Abrir um Pull Request (PR)**
1. No GitHub, vá até a página do seu repositório.
2. Clique em **"Compare & pull request"** ao lado da branch que você acabou de enviar.
3. Descreva as alterações feitas no PR:
   - O que foi implementado?
   - Como foi testado?
   - Quais issues estão relacionadas?
4. Atribua um revisor (outro membro do time) para revisar o PR.

---

### 5. **Revisar e Aprovar um PR**
1. Como revisor, acesse o PR e analise as alterações.
2. Faça comentários específicos se houver algo a ser ajustado.
3. Se tudo estiver correto, aprove o PR clicando em **"Approve"**.
4. O autor do PR pode fazer o merge após a aprovação.

---

### 6. **Atualizar o Repositório Local**
Após o merge, atualize sua branch `main` local com as alterações mais recentes:
1. Navegue para a branch `main`:
   ```bash
   git checkout main
   ```
2. Puxe as atualizações:
   ```bash
   git pull origin main
   ```

---

### 7. **Boas Práticas**
- Sempre crie branches para novas funcionalidades ou correções.
- Escreva mensagens de commit claras e descritivas.
- Revise o código dos colegas com atenção e faça comentários construtivos.
- Mantenha o repositório organizado e documentado.

---

Agora é só começar a codar! 🚀
