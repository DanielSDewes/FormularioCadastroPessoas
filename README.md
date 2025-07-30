
# 📋 Projeto: Cadastro de Pessoas

Este é um sistema simples de cadastro de pessoas com interface web. O usuário pode inserir nome, CPF e endereço, e o sistema completa automaticamente os campos de endereço ao informar o CEP. As validações são feitas tanto no backend (CPF válido) quanto no frontend (formulário dinâmico sem recarregamento).

## 🚀 Tecnologias Utilizadas

- **Python 3**
  - Framework: [Flask](https://flask.palletsprojects.com/)
  - Requisições HTTP: [Requests](https://pypi.org/project/requests/)
- **HTML5** — Estrutura da interface
- **CSS3** — Estilização básica da interface
- **JavaScript (ES6+)**
  - Manipulação do DOM
  - Requisições AJAX com `fetch()`
- **API pública ViaCEP**
  - Usada para buscar dados de endereço a partir do CEP digitado

## 🔧 Funcionalidades

- Cadastro de pessoas com:
  - Nome
  - CPF (validação de formato e dígitos verificadores)
  - Endereço automático via CEP
- Exclusão de registros
- Validação de campos obrigatórios
- Mensagens de sucesso ou erro exibidas dinamicamente na interface

## 🛠️ Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/DanielSDewes/FormularioCadastroPessoas
cd seu-repositorio
```

### 2. Instale as dependências

Certifique-se de que o **Python 3** e o **pip** estão instalados.

```bash
pip install flask requests
```

### 3. Crie o banco de dados

Execute o script que cria o banco de dados SQLite (`database.db`):

```bash
python models.py
```

### 4. Inicie o servidor Flask

```bash
python app.py
```

### 5. Acesse no navegador

Abra o navegador e vá até:

```
http://127.0.0.1:5000
```

## 📦 Estrutura do Projeto

```
📁 seu-projeto/
├── app.py             # Servidor Flask
├── models.py          # Criação do banco de dados
├── database.db        # Banco de dados SQLite gerado
├── templates/
│   └── index.html     # Interface HTML
├── static/
│   ├── style.css      # Estilos da página
│   └── script.js      # Lógica JS (CEP, envio AJAX, mensagens)
```

## 📡 API Utilizada

- [ViaCEP - https://viacep.com.br](https://viacep.com.br)
  - Endpoint: `https://viacep.com.br/ws/<CEP>/json/`
  - Gratuita, sem necessidade de autenticação

## ✨ Melhorias Futuras (sugestões)

- Validação de duplicidade de CPF
- Paginação de resultados
- Edição de registros
- Login de usuários (autenticação)

---

## 🧑‍💻 Autor

Daniel Dewes – [@DanielSDewes](https://github.com/DanielSDewes)
