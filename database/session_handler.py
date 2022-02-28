from database import get_session


def get_object(model, **kwargs):
    session = get_session()
    obj = session.query(model).filter_by(**kwargs).first()
    return obj

def save_object(obj):
    session = get_session()
    session.add(obj)
    session.commit()

