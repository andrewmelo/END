from database import get_session


def get_object(model, **kwargs):
    session = get_session()
    obj = session.query(model).filter_by(**kwargs).first()
    session.close()
    return obj

def save_object(obj):
    session = get_session()
    session.add(obj)
    session.commit()

def transaction(account, value, operation):
    session = get_session()
    account = account
    if operation == "deposit":
        account.checking += value
    elif operation == "withdraw":
        account.checking -= value
    session.add(account)
    session.commit()
