# Projeto-DevOps

![CI](https://github.com/fcoli/Projeto-DevOps/actions/workflows/ci.yml/badge.svg)

Projeto simples criado para praticar conceitos de DevOps: controle de
versao com Git/GitHub (branches, commits e pull requests) e integracao
continua (CI) com GitHub Actions.

## Sobre

Um gerenciador de tarefas (task manager) via linha de comando, escrito
em Python, com testes automatizados e um pipeline de CI que roda os
testes a cada push e a cada pull request.

## Como usar

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Comandos disponiveis:

```bash
python app.py add "Estudar DevOps"
python app.py list
python app.py done 1
python app.py remove 1
```

## Rodando os testes

```bash
pytest -v
```

## Estrutura do projeto

```
app.py                     # logica principal do gerenciador de tarefas
tests/test_app.py          # testes unitarios
requirements.txt           # dependencias do projeto
.github/workflows/ci.yml   # pipeline de integracao continua (CI)
```

## Fluxo de trabalho utilizado

- Desenvolvimento realizado no branch `CI`, separado do `main`.
- Multiplos commits pequenos e descritivos.
- Integracao via Pull Request do branch `CI` para o `main`.

## Notificacoes

Este repositorio envia um alerta para um canal do Discord a cada push no
branch `main` (veja `.github/workflows/discord-notify.yml`).
