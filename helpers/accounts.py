from models.account_model import AccountModel
from database import get_session

def get_account_by_user_id(user_id: int) -> AccountModel:
    user_id = AccountModel()
    return user_id