from flask_login import UserMixin

from src.infrastructure.repositories.user_repository import UserRepository

class UserData:
    def __init__(self, email, username, password, is_admin):
        self.username = username
        self.password = password
        self.email = email
        self.is_admin = is_admin

class UserModel(UserMixin):
    def __init__(self, user_data: UserData):
        self.id = user_data.username
        self.email = user_data.email
        self.password = user_data.password
        self.is_admin = user_data.is_admin
    
    @staticmethod
    def query(user_id):
        user_repository = UserRepository()
        user = user_repository.get_user_by_username(user_id)
        user_data = UserData(user.email, user.username, user.password, user.is_admin)
        
        return UserModel(user_data)