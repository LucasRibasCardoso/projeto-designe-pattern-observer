# Sistema de Podcasts - Padrão Observer

Sistema desenvolvido em Python que implementa o padrão de projeto **Observer** para simular a distribuição de episódios de podcast entre um catálogo central (Publisher) e múltiplos clientes/agregadores (Subscribers).

## 📋 Descrição

Este projeto demonstra a aplicação prática do padrão Observer em um cenário real: um sistema de distribuição de podcasts onde:

- Um **catálogo central** publica novos episódios automaticamente em intervalos aleatórios
- **Múltiplos clientes** (como Spotify, Apple Podcasts, etc.) são notificados automaticamente sobre novos episódios
- Cada cliente mantém seu próprio **catálogo local** com os episódios recebidos
- A comunicação é **unidirecional**: do Publisher para os Subscribers

## 🏗️ Estrutura do Projeto

```
projeto-designe-pattern-observer/
│
├── observer.py              # Interfaces Observer e Subject
├── podcast_catalogo.py      # Implementação do Publisher
├── cliente_podcast.py       # Implementação do Subscriber
├── main.py                  # Aplicação principal com menu interativo
├── RELATORIO.txt           # Relatório detalhado da implementação
└── README.md               # Este arquivo
```

## 🎯 Padrão Observer

### Componentes

1. **Subject (Publisher)** - `PodcastCatalogo`:
   - Mantém lista de episódios
   - Gerencia subscribers registrados
   - Notifica automaticamente sobre novos episódios

2. **Observer (Subscriber)** - `ClientePodcast`:
   - Recebe notificações do Publisher
   - Mantém catálogo local de episódios
   - Armazena metadata (data/hora de recebimento)

### Fluxo de Comunicação

```
Publisher (PodcastCatalogo)
    │
    ├─ Gera novo episódio (intervalo aleatório 5-15s)
    │
    ├─ notify() ────┬──> Subscriber 1 (Spotify)
    │               │         └─> update(episodio)
    │               │                 └─> Adiciona ao catálogo local
    │               │
    │               ├──> Subscriber 2 (Apple Podcasts)
    │               │         └─> update(episodio)
    │               │                 └─> Adiciona ao catálogo local
    │               │
    │               └──> Subscriber N...
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior

### Execução

```bash
python main.py
```

### Menu Interativo

O sistema apresenta um menu com as seguintes opções:

1. **Consultar episódios do catálogo local** - Visualiza os episódios de um cliente específico
2. **Exibir informações do sistema** - Mostra estatísticas gerais
3. **Adicionar novo cliente** - Registra um novo subscriber dinamicamente
4. **Limpar catálogo local** - Remove episódios de um cliente
5. **Sair** - Encerra o sistema

## 📦 Funcionalidades

### Publisher (PodcastCatalogo)

- ✅ Publicação automática de episódios em intervalos aleatórios
- ✅ Gerenciamento de múltiplos subscribers
- ✅ Notificação automática e imediata
- ✅ Execução em thread separada (não bloqueia o menu)

### Subscriber (ClientePodcast)

- ✅ Recebimento automático de notificações
- ✅ Catálogo local independente
- ✅ Registro de timestamp de recebimento
- ✅ Métodos de consulta e gerenciamento

### Sistema

- ✅ Menu interativo em loop infinito
- ✅ Suporte a múltiplos clientes simultâneos
- ✅ Adição dinâmica de novos subscribers
- ✅ Tratamento de exceções e interrupções

## 📊 Exemplo de Saída

```
============================================================
SISTEMA DE PODCASTS - PADRÃO OBSERVER
============================================================
[PUBLISHER] Novo subscriber registrado. Total: 2
[PUBLISHER] PodcastHub iniciado - Publicando episódios automaticamente

[PUBLISHER] Novo episódio disponível: episodio01
[PUBLISHER] Notificando 2 subscriber(s) sobre: episodio01
  → [Spotify] Episódio recebido: episodio01
  → [Apple Podcasts] Episódio recebido: episodio01

============================================================
SISTEMA DE PODCASTS - PADRÃO OBSERVER
============================================================
1. Consultar episódios do catálogo local
2. Exibir informações do sistema
3. Adicionar novo cliente (subscriber)
4. Limpar catálogo local
5. Sair
============================================================
```

## 🎓 Conceitos Demonstrados

### Padrão Observer

- ✅ Separação entre Subject e Observer
- ✅ Comunicação um-para-muitos
- ✅ Notificação automática de mudanças
- ✅ Baixo acoplamento entre componentes

### Programação Orientada a Objetos

- ✅ Abstração com classes abstratas
- ✅ Encapsulamento de dados e comportamentos
- ✅ Polimorfismo através de interfaces
- ✅ Composição de objetos

### Python

- ✅ Módulo `abc` para classes abstratas
- ✅ Threading para execução paralela
- ✅ Type hints para melhor documentação
- ✅ Boas práticas de organização de código

## 📝 Requisitos Atendidos

- ✅ Publisher mantém lista de episódios
- ✅ Atualização em intervalos aleatórios
- ✅ Notificação automática de subscribers
- ✅ Subscriber mantém catálogo local
- ✅ Recebimento via notificações (não polling)
- ✅ Menu em loop infinito
- ✅ Comunicação unidirecional (Publisher → Subscriber)
- ✅ Relatório explicativo em TXT

## 📖 Documentação Adicional

Consulte o arquivo [RELATORIO.txt](RELATORIO.txt) para uma explicação detalhada sobre:

- Contextualização do problema
- Estrutura completa do padrão
- Fluxo de comunicação
- Benefícios da implementação
- Comparação com outros padrões

## 🤝 Contribuições

Este é um projeto educacional desenvolvido para demonstrar o padrão Observer. Sugestões e melhorias são bem-vindas!

## 📄 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

---

**Desenvolvido com 💙 usando Python e o padrão Observer**