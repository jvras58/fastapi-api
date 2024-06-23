<h1 align="center">
  <a href="">Projeto de API com FASTAPI</a>
</h1>

<p align="center">
  <a href="#memo-requisitos">Requisitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#information_source-como-usar">Como usar</a>
</p>

## :memo: Requisitos

| Ferramenta                                         | Versão  | Descrição                                   |
| -------------------------------------------------- | ------- | ------------------------------------------- |
| [Poetry](https://python-poetry.org/)               | -       | gerenciador dependências em projetos Python |
| [Python](https://www.python.org/)                  | -       | Linguagem de desenvolvimento                |
| [Git](https://git-scm.com)                         | -       | Controle de versões                         |
| [SQLite](https://sqlite.org/)                      | -       | Sistema de gerenciamento de banco de dados  |


## :rocket: Tecnologias

Este projeto está sendo desenvolvido com:

- Gerenciador: [Poetry](https://python-poetry.org/)
- Linguagem e ambiente: [Python](https://www.python.org/)
- Object-Relation-Mapper (ORM): [SQLAlchemy](https://www.sqlalchemy.org/)
- Banco de dados: [SQLite](https://sqlite.org/)


## :information_source: Como usar

```bash
# Clonar este repositório
$ git clone {link_deste_repositorio}

# Ir para o repositório
$ cd {pasta_deste_repositorio}

# Criar o arquivo .env com os valores adequados ao ambiente. pasta .secrets precisa ter (TESTE_SECRET).
$ cp .env-semple .env

# Entre no ambiente virtual
$ poetry shell

# Instalar as dependências
$ poetry install

# Executar as migrations
  $ alembic upgrade head

# Executar a api
$ task run

# teste a api
$ task test
```

- Endereço local: (http://localhost:8000)


---
