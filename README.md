# Explicador de Conteúdo de Inglês

Programa interativo em Python que explica conteúdos teóricos de inglês de acordo com o nível de aprendizado do usuário (baseado no Quadro Europeu Comum de Referência: A1, A2, B1, B2, C1, C2).

## Como funciona

Ao rodar o programa, o usuário informa seu nome e escolhe um nível de inglês em um menu. Dentro de cada nível, é possível escolher um tópico específico (ex: Verb To Be, Present Simple, Modal Can/Can't) e receber uma explicação sobre o assunto.

## Como rodar

```bash
python menu.py
```

Não há dependências externas até o momento — usa apenas bibliotecas padrão do Python.

## Estrutura do projeto

```
menu.py              -> Menu principal, interação com o usuário
explicacoesA1.py      -> Conteúdos do nível A1 (Iniciante)
explicacoesA2.py      -> Conteúdos do nível A2 (Básico)
explicacoesB1.py      -> Conteúdos do nível B1 (Intermediário)
explicacoesB2.py      -> Conteúdos do nível B2 (Intermediário Avançado)
explicacoesC1.py      -> Conteúdos do nível C1 (Avançado)
explicacoesC2.py      -> Conteúdos do nível C2 (Fluência)
```

## Status atual

- [x] Menu interativo com todos os níveis e navegação
- [x] Validação de entrada do usuário
- [x] Conteúdo do nível A1 implementado
- [ ] Conteúdo dos níveis A2, B1, B2, C1, C2 (em andamento)
- [ ] Integração com IA para gerar exercícios e correções

## Próximos passos

- Preencher os conteúdos teóricos dos demais níveis
- Adicionar exercícios de fixação por tópico
- Integrar API de IA para correção automática de respostas e explicações alternativas