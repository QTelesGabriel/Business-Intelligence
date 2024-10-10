from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import crud.crud as crud
from fastapi import FastAPI
import uvicorn

# Definindo a URL do banco de dados
DATABASE_URL = "sqlite:///base_tarefas.db"
engine = create_engine(DATABASE_URL)

# Criando uma sessão para conectar ao banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Configurando o FastAPI
app = FastAPI()

@app.get('/leitura_tabela')
def ler_tabela(entidade:int):
    if entidade == 1:
        return crud.read_users(session)
    if entidade == 2:
        return crud.read_tasks(session)

@app.post('/create_user')
def create_user(nome:str, gmail:str):
    crud.create_user(session, nome, gmail)
    return crud.read_users(session)

@app.post('/create_task')
def create_task(task:str, priority:str, status:str, userID:int):
    crud.create_task(session, task, priority, status, userID)
    return crud.read_tasks(session)

@app.delete('/delete_user')
def delete_user(id:int):
    crud.delete_user(session, id)
    return crud.read_users(session)

@app.delete('/delete_task')
def delete_task(id:int):
    crud.delete_task(session, id)
    return crud.read_tasks(session)

@app.put('/update_user')
def update_user(userID:int, new_name:str, new_email:str):
    crud.update_user(session, userID, new_name, new_email)
    return crud.read_users(session)

@app.put('/update_task')
def update_task(taskID:int, new_task:str, new_priority:str, new_status:str, new_userID:int):
    crud.update_task(session, taskID, new_task, new_priority, new_status, new_userID)
    return crud.read_tasks(session)

# Testando as operações de CRUD
if __name__ == "__main__":
    # Abrindo a conexão
    # uvicorn controlador:app --port 8888 --reload
    uvicorn.run("controlador:app", port=8888, reload=True)
    try:
        # # Criar alguns usuários
        # crud.create_user(session, "João", "joao@gmail.com")
        # crud.create_user(session, "Maria", "maria@gmail.com")
        
        # # Criar algumas tarefas
        # crud.create_task(session, "Terminar projeto", "Alta", "Em Progresso", 1)
        # crud.create_task(session, "Comprar mantimentos", "Baixa", "Pendente", 2)

        # # Listar todos os usuários
        # print("\n--- Lista de Usuários ---")
        # crud.list_all_users(session)

        # # Listar todas as tarefas
        # print("\n--- Lista de Tarefas ---")
        # crud.list_all_tasks(session)

        # # Ler um usuário específico
        # print("\n--- Ler Usuário Específico ---")
        # crud.list_user(session, 1)

        # # Ler uma tarefa específica
        # print("\n--- Ler Tarefa Específica ---")
        # crud.list_task(session, 1)

        # # Atualizar um usuário
        # print("\n--- Atualizar Usuário ---")
        # crud.update_user(session, 1, "João Silva", "joaosilva@gmail.com")

        # # Atualizar uma tarefa
        # print("\n--- Atualizar Tarefa ---")
        # crud.update_task(session, 1, "Finalizar projeto com cliente", "Alta", "Concluída", 1)

        # # Excluir um usuário
        # print("\n--- Excluir Usuário ---")
        # crud.delete_user(session, 2)  # Excluir Maria

        # # Excluir uma tarefa
        # print("\n--- Excluir Tarefa ---")
        # crud.delete_task(session, 2)  # Excluir tarefa "Comprar mantimentos"

        # # Listar novamente após as alterações
        # print("\n--- Lista de Usuários Atualizada ---")
        # crud.list_all_users(session)

        # print("\n--- Lista de Tarefas Atualizada ---")
        # crud.list_all_tasks(session)
        print("Conexão na porta 8888 fechada")

    finally:
        # Fechar a conexão
        session.close()
        print("\nConexão com o banco de dados fechada.")
