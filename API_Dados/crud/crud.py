from data_models.models import User, Task
from datetime import datetime

def create_user(session, name, email):
    with session:
        new_user = User(name=name, email=email, created=datetime.now())
        session.add(new_user)
        session.commit()
        print(f"Usuário {name} adicionado com sucesso.")

def create_task(session, task, priority, status, userID):
    with session:
        nova_task = Task(created=datetime.now(), updated=datetime.now(), task=task, priority=priority, status=status, userID=userID)
        session.add(nova_task)
        session.commit()
        print(f"Tarefa '{task}' adicionada com sucesso para o usuário {userID}.")

def read_user(session, id):
    with session:
        return session.query(User).filter_by(id=id).first()

def list_user(session, userID):
    with session:
        user = read_user(session, userID)
        if user:
            print(f"ID: {user.id}, Nome: {user.name}, Email: {user.email}, Criado em: {user.created}")
        else:
            print(f"User com ID {userID} não encontrado.")

def list_all_users(session):
    with session:
        users = session.query(User).all()
        for user in users:
            print(f"ID: {user.id}, Nome: {user.name}, Email: {user.email}, Criado em: {user.created}")

def read_task(session, id):
    with session:
        return session.query(Task).filter_by(id=id).first()

def list_task(session, taskID):
    with session:
        task = read_task(session, taskID)
        if task:
            print(f"ID: {task.id}, Tarefa: {task.task}, Status: {task.status}, Usuário ID: {task.userID}, Criada em: {task.created}, Atualizada em: {task.updated}")
        else:
            print(f"Tarefa com ID {taskID} não encontrada.")

def list_all_tasks(session):
    with session:
        tasks = session.query(Task).all()
        for task in tasks:
            print(f"ID: {task.id}, Tarefa: {task.task}, Prioridade: {task.priority}, Status: {task.status}, Atualizado em: {task.updated}, Usuário ID: {task.userID}")

def update_user(session, userID, new_name, new_email):
    with session:
        user = read_user(session, userID)
        if user:
            user.name = new_name
            user.email = new_email
            session.commit()
    
def update_task(session, taskID, new_task, new_priority, new_status, new_userID):
    with session:
        task = read_task(session, taskID)
        if task:
            task.task = new_task
            task.priority = new_priority
            task.status = new_status
            task.userID = new_userID
            task.updated = datetime.now()
            session.commit()

def delete_user(session, id):
    with session:
        user = read_user(session, id)
        if user:
            session.delete(user)
            session.commit()

def delete_task(session, id):
    with session:
        task = read_task(session, id)
        if task:
            session.delete(task)
            session.commit()