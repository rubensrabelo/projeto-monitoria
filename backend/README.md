## Diagrama de classes

```mermaid
classDiagram

class Question {
    id: str
    question: str
    sql: str
    dataset: str
    answer: Answer
    created_at: datetime
    updated_at: datetime
}

class Answer {
    columns: list[str] 
    rows: list[list[SQLValue]] 
    execution_time: float
}

Question *-- Answer
```

## Estrutura de dados

```bash
monitoria-projeto
│
├── src
│   ├── api
│   │   ├── routes
│   │   │   ├── dataset_routes.py
│   │   │   └── query_routes.py
│   │
│   ├── services
│   │   ├── dataset_service.py
│   │   └── query_service.py
│   │
│   ├── core
│   │   └── duckdb_manager.py
│   │
│   ├── schemas
│   │   └── query_schema.py
│   │
│   └── main.py
│
├── datasets
│
├── requirements.txt
```