from sqlalchemy.orm import Session
from app.repositories import user as user_repo
from passlib.hash import bcrypt

def register_user(cpf:str, name: str, password: str):
    existing = user_repo.get_user_by_cpf(cpf)
    if existing:
        return None
    hashed = bcrypt.hash(password)
    return user_repo.create_user(cpf, name, hashed)
