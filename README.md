# TaskFlow Manager

## Descrição do Projeto

O TaskFlow Manager é um sistema web básico de gerenciamento de tarefas desenvolvido para simular o acompanhamento de atividades de uma equipe de logística. O sistema permite criar, listar, atualizar e excluir tarefas, auxiliando no controle do fluxo de trabalho.

## Objetivo

O objetivo do projeto é aplicar conceitos de Engenharia de Software, metodologias ágeis, versionamento com Git/GitHub, testes automatizados e integração contínua com GitHub Actions.

## Escopo Inicial

O escopo inicial do sistema inclui:

- Cadastro de tarefas
- Listagem de tarefas
- Atualização do status das tarefas
- Exclusão de tarefas
- Testes automatizados com Pytest
- Pipeline de CI com GitHub Actions

## Metodologia Ágil Utilizada

A metodologia utilizada foi o Kanban, pois permite visualizar o andamento das tarefas por meio de colunas como:

- To Do
- In Progress
- Done

Essa abordagem ajuda na organização do trabalho, no acompanhamento do progresso e na identificação de tarefas pendentes.

## Mudança de Escopo

Durante o desenvolvimento, foi simulada uma mudança de escopo solicitada pelo cliente: a inclusão do campo de status nas tarefas.

Justificativa: o cliente precisava acompanhar melhor o andamento das atividades da equipe, identificando quais tarefas estavam pendentes, em andamento ou concluídas.

Essa alteração foi adicionada ao Kanban como uma nova tarefa e implementada no código por meio da função de atualização de status.

## Tecnologias Utilizadas

- Python
- Flask
- Pytest
- GitHub
- GitHub Projects
- GitHub Actions

## Como Executar o Projeto

Clone o repositório:

```bash
git clone https://github.com/guilhermemaciel0/taskflow-manager