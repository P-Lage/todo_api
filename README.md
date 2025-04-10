# 📝 API RESTful de Tarefas (To-Do List)

Uma API simples para gerenciamento de tarefas, desenvolvida com **FastAPI**, **SQLAlchemy** e **SQLite**.

---

## 🚀 Funcionalidades

- Criar tarefas
- Listar tarefas (com filtro por status, paginação e ordenação)
- Atualizar tarefas (título, status)
- Deletar tarefas
- Campos adicionais: `created_at`, `updated_at`, `due_date`
- Migrations com Alembic
- Testes com pytest

---

## 📦 Instalação

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual e ative:

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Execute as migrations:

```
alembic upgrade head
```

5. Inicie o servidor:

```
uvicorn app.main:app --reload
```

## 🔍 Exemplos de uso

### Criar tarefa

```
POST /tasks/
{
  "title": "Estudar FastAPI",
  "completed": false,
  "due_date": "2025-04-10T23:59:00"
}
```

### Atualizar tarefa

```
PATCH /tasks/1
{
  "completed": true
}
```

### Listar tarefas com filtros

```
GET /tasks?completed=false&skip=0&limit=10&order_by=created_at
```

### Rodando testes

```
pytest
```

## 🌍 Deploy
🔗 API online (em breve)

## 📄 Licença
MIT
