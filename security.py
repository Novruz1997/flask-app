from models.user import UserModel
# from werkzeug.security import safe_str_cmp
from hmac import compare_digest


def authenticate(username, password):
    # user = username_mapping.get(username, None)
    user = UserModel.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)





