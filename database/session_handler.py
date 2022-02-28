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

def transaction(bank_account, value, operation):
    session = get_session()
    if operation == "deposit":
        bank_account.checking += value
    elif operation == "withdraw":
        bank_account.checking -= value
    session.add(bank_account)
    session.commit()
