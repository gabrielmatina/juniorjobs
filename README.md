# JuniorJobs

## Resumo

O **JuniorJobs** é uma plataforma de aplicação para vagas de emprego, projetada para conectar candidatos a vagas de emprego e empresas que procuram contratar novos talentos. O sistema permite que administradores gerenciem o sistema, recrutadores publiquem vagas e candidatos se candidatem a essas vagas.

## Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o Python 3.6+ instalado na sua máquina. Além disso, é recomendável usar um ambiente virtual para gerenciar as dependências do projeto.

### Passos para Configuração

1. **Clone o repositório:**
   ```bash
   # HTTPS
   git clone https://github.com/seu-usuario/juniorjobs.git
   # SSH
   git clone git@github.com:gabrielmatina/juniorjobs.git 
   cd juniorjobs
   
   ```
2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv .venv
   # No Windows
   .\.venv\Scripts\activate
   # No macOS/Linux
   source .venv/bin/activate
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. Configure o banco de dados:
   ```bash
   python manage.py migrate
   ```
5. Crie um superusuário:
    ```bash
    python manage.py createsuperuser
    ```
6. Rode o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
Acesse o projeto no seu navegador em http://127.0.0.1:8000.
    
### Ferramentas Utilizadas
    - Django: Framework web feito em Python que permite o desenvolvimento rápido e seguro de aplicações.
    - SQLite: Banco de dados relacional que por padrão vem incluso no projeto.
    - Bootstrap: Framework CSS para estilização do frontend.

## Funcionalidades

- **Sistema de Autenticação**: Registre-se, fazer login.
- **Perfis de Usuário**:
  - **Administrador do Sistema**: Gerencia todo o sistema.
  - **RH da Empresa**: Publica e gerencia vagas de emprego.
  - **Candidato**: Visualiza e se candidata a vagas de emprego.
- **Gerenciamento de Vagas**: RH pode criar, editar e deletar vagas.
- **Candidatura a Vagas**: Candidatos podem se inscrever em vagas disponíveis.

## Rotas do Projeto

- **/admin/**: Acesso ao painel administrativo do Django.
- **/**: Pagina Home.
- **/login/**: Página de login de usuário.
- **/register/**: Página de registro de candidato.
- **/available-jobs/**: Lista de todas as vagas disponíveis.
- **/applied-jobs/**: Detalhes das vagas aplicadas.
- **/add-job/**: Página para criar uma nova vaga.
- **/view-jobs/**: Página para visualizar todas as vagas em aberto.
- **/reports/**: Página de relatórios.

## O que Falta a Ser Desenvolvido

- **Lógica de separar o candidato e o recrutador**: Infelizmente não consegui desenvolver o formulário para que o sistema identifique de forma automatica se o cadatro está sendo feito é de um candidato ou a pessoa é o recrutador da empresa.
- **Implemetação das funcinalidades**: Criei as rotas, os tampletes porém não desenvolvi as funcionalidades:
    - Listar todas as vagas
    - O candidato visualizar todas as vagas que ele se candidatou.
    - Pagina para o recrutador criar uma nova vaga
    - Página para o recrutador visualizar todas as vagas e poder editar essas vagas ou exclui-las.
    - Relatórios
    - Qualificar os candidatos em relação a cada uma das vagas.

## Futuras implementações
Implementar funcionalidades de busca e filtragem para candidatos.
- **Perfil de Empresa**: Adicionar perfis detalhados para empresas.
- **Comentários e Feedback**: Permitir que recrutadores deixem feedback sobre candidatos.
- **Esqueci Minha Senha**: Enviar via E-mail o passo a passo de como um candidato ou recrutador pode recuperar o seu acesso junto a plataforma.
- **Layout**: Melhorar o layout do projeto.

## Conclusão

O projeto **JuniorJobs** tem como objetivo simplificar o processo de recrutamento e candidatura, proporcionando uma interface amigável tanto para candidatos quanto para recrutadores. Apesar das funcionalidades já implementadas, há espaço para muitas melhorias e expansões que podem tornar a plataforma ainda mais robusta e útil.
