from database import get_session
from sqlalchemy.exc import SQLAlchemyError

def select_one_from(model, user_id):
    try:
        session = get_session()
        obj = session.query(model).get(user_id)
        session.close()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)
        return
    return obj

def select_all_from_where(model, user_id):
    try:
        session = get_session()
        objs = session.query(model).filter_by(user_id=user_id).all()
        return objs
    except SQLAlchemyError as e:
        session.rollback()
        print(e)

def insert_into(obj):
    try:
        session = get_session()
        session.add(obj)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)

def delete_character(model, character_name):
    try:
        session = get_session()
        obj = session.query(model).filter(character_name=character_name)
        session.delete(obj)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)

def select_all_from_table(model):
    try:
        session = get_session()
        objs = []
        for obj in session.query(model).all():
            objs.append(obj)
        return objs
    except SQLAlchemyError as e:
        session.rollback()
        print(e)