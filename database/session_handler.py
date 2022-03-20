from database import get_session
from sqlalchemy.exc import SQLAlchemyError

def select_from(model, user_id):
    try:
        session = get_session()
        obj = session.query(model).get(user_id)
        session.close()
    except SQLAlchemyError as e:
        print(e)
        session.close()
        return
    return obj

def insert_into(obj):
    try:
        session = get_session()
        session.add(obj)
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        print(e)
        session.close()

def transaction(player, value, operation):
    try:  
        session = get_session()
        if operation == "deposit":
            player.checking_account += value
        elif operation == "withdraw":
            player.checking_account -= value
        session.add(player)
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        print(e)
        session.close()
