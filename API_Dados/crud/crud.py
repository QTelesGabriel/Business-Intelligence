from data_models.models import User, Task
from sqlalchemy import update
from datetime import datetime

def create_user(session, name, email):
    with session:
        new_user = User(name=name, email=email, created=datetime.now())
        session.add(new_user)
        session.commit()
        print(f"Usuário {name} adicionado com sucesso.")

def create_task(session, task, priority, status, userID):
    with session:
        new_task = Task(created=datetime.now(), updated=datetime.now(), task=task, priority=priority, status=status, userID=userID)
        session.add(new_task)
        session.commit()
        print(f"Tarefa '{task}' adicionada com sucesso para o usuário {userID}.")

def read_user(session, id):
    with session:
        return session.query(User).filter_by(id=id).first()

def read_users(session):
    with session:
        return session.query(User).all()

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

def read_tasks(session):
    with session:
        return session.query(Task).all()

def list_task(session, taskID):
    with session:
        task = read_task(session, taskID)
        if task:
            print(f"ID: {task.id}, Tarefa: {task.task}, Status: {task.status}, Usuário ID: {task.userID}, Criada em: {task.created}, Atualizada em: {task.updated}")
        else:
            print(f"Tarefa com ID {taskID} não encontrada.")

def list_all_tasks(session):
    with session:
        tasks = read_tasks(session)
        for task in tasks:
            print(f"ID: {task.id}, Tarefa: {task.task}, Prioridade: {task.priority}, Status: {task.status}, Atualizado em: {task.updated}, Usuário ID: {task.userID}")

def update_user(session, userID, new_name, new_email):
    with session:
        user = read_user(session, userID)
        if user:
            stmt = (
                update(User).
                where(User.id == userID).
                values(name=new_name, email=new_email)
            )
            session.execute(stmt)
            session.commit()
    
def update_task(session, taskID, new_task, new_priority, new_status, new_userID):
    with session:
        task = read_task(session, taskID)
        if task:
            stmt = (
                update(Task).
                where(Task.id == taskID).
                values(task=new_task, priority=new_priority, status=new_status, userID=new_userID)
            )
            session.execute(stmt)
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
