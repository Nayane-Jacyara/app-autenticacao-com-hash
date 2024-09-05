# Sistema de Autenticação 

Este projeto é uma atividade acadêmica da disciplina de Segurança da Informação. O objetivo é desenvolver um sistema de autenticação com foco na segurança das senhas dos usuários, utilizando criptografia e armazenamento seguro em um banco de dados SQLite.

## Objetivo

A atividade tem como objetivo implementar um sistema de autenticação que garante a segurança das senhas dos usuários. Para isso, o sistema utiliza criptografia para armazenar as senhas de forma segura e permite o gerenciamento de usuários por meio de uma interface administrativa.

## Funcionalidades

- **Cadastro de Usuários**: Permite que novos usuários se cadastrem no sistema com validação de senha.
- **Login de Usuários**: Permite que usuários façam login utilizando seu nome e senha.
- **Gerenciamento de Usuários**: Interface administrativa para visualizar e gerenciar os usuários cadastrados.
- **Listagem de Usuários**: Exibe uma lista de usuários cadastrados (para fins de desenvolvimento).

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **Flask-SQLAlchemy**: ORM para gerenciamento do banco de dados SQLite.
- **Flask-Bcrypt**: Para criptografia e segurança das senhas.
- **Flask-WTF**: Para criação e validação de formulários.
- **Flask-Admin**: Para gerenciamento de usuários com uma interface administrativa.
- **SQLite**: Banco de dados para armazenamento de dados.

## Explicação do Código

1. **Configuração Inicial**:
   - O Flask é inicializado e configurado com uma chave secreta e a URI do banco de dados SQLite.
   - O `SQLAlchemy` é usado para gerenciar a conexão com o banco de dados e as operações de CRUD.
   - O `Bcrypt` é utilizado para criptografar as senhas dos usuários.

2. **Modelo de Usuário**:
   - A classe `Usuario` define a estrutura do banco de dados, com campos para `id`, `nome` e `senha`.

3. **Formulários**:
   - `CadastroForm` e `LoginForm` são definidos utilizando `Flask-WTF` para gerenciar a entrada de dados dos usuários e realizar validações.

4. **Rotas**:
   - `/`: Página inicial do aplicativo.
   - `/cadastro`: Página para cadastro de novos usuários.
   - `/login`: Página para login de usuários existentes.
   - `/dashboard`: Página de boas-vindas após o login.
   - `/usuarios`: Página para listar todos os usuários cadastrados (usada para desenvolvimento).

5. **Criação do Banco de Dados**:
   - O banco de dados e suas tabelas são criados automaticamente na primeira execução da aplicação.
