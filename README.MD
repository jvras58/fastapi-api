Aqui está uma versão aprimorada do README, com mais detalhes e melhorias na formatação:

<h1 align="center">
  <a href="">Projeto de API com FASTAPI</a>
</h1>

<p align="center">
  <a href="#memo-requisitos">Requisitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#information_source-como-usar">Como Usar</a>
</p>

## :memo: Requisitos

Para executar este projeto, você precisará das seguintes ferramentas:

| Ferramenta                                         | Versão  | Descrição                                   |
| -------------------------------------------------- | ------- | ------------------------------------------- |
| [Poetry](https://python-poetry.org/)               | 1.8.2   | Gerenciador de dependências para projetos Python |
| [Python](https://www.python.org/)                  | 3.11    | Linguagem de programação                    |
| [Jinja2](https://jinja.palletsprojects.com/)       | 3.1.4   | templating engine                           |
| [Alembic](https://alembic.sqlalchemy.org/)         | 1.12.0  | migração de banco de dados para uso com o SQLAlchemy |
| [SQLAlchemy](https://www.sqlalchemy.org/)          | 2.0.22  | kit de ferramentas Python SQL (ORM)         |
| [pydantic](https://docs.pydantic.dev/latest/)      | 2.4.2   | biblioteca de validação de dados            |
| [Git](https://git-scm.com)                         | -       | Sistema de controle de versões              |
| [SQLite](https://sqlite.org/)                      | -       | Sistema de gerenciamento de banco de dados  |


## :rocket: Tecnologias

Este projeto utiliza as seguintes tecnologias:

- **Gerenciador de dependências:** [Poetry](https://python-poetry.org/)
- **Linguagem e ambiente de desenvolvimento:** [Python](https://www.python.org/)
- **Templete engine para o front-end** [Jinja2](https://jinja.palletsprojects.com/)
- **ORM (Object-Relational Mapper):** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Banco de dados:** [SQLite](https://sqlite.org/)


## :information_source: Como Usar

Siga as instruções abaixo para configurar e executar o projeto:

```bash
# Clone este repositório
git clone https://github.com/jvras58/fastapi-api.git

# Navegue até o diretório do projeto
cd fastapi-api

# Crie o arquivo .env com os valores adequados ao ambiente
cp .env-sample .env

# Cria a pasta .secrets
$ mkdir .secrets

# Cria o arquivo TESTE_SECRET dentro da pasta .secrets e adiciona o conteúdo TESTE_SECRET
$ echo "TESTE_SECRET" > .secrets/TESTE_SECRET

# Entre no ambiente virtual gerenciado pelo Poetry
poetry shell

# Instale as dependências do projeto
poetry install

# Execute as migrações do banco de dados
alembic upgrade head

# Execute os testes para verificar se a API está funcionando corretamente
task test

# Inicie a API
task run
```

- A API estará disponível localmente em: [http://localhost:8000/](http://localhost:8000/)
- O frontend pode ser acessado em: [http://localhost:8000/template/index](http://localhost:8000/template/create_user)

## :handshake: Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## :page_facing_up: Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

<p align="center">Desenvolvido com :heart: por jvras</p>
