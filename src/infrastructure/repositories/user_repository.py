from src.domain.repositories.user_repository_interface import UserRepositoryInterface
from src.infrastructure.schema.user_schema import UserSchema


class UserRepository(UserRepositoryInterface):
    def get_user_by_username_and_password(self, username, password):
        user = UserSchema.query.filter_by(username = username, password = password).first()
        return user

    def get_user_by_username(self, username):
        user = UserSchema.query.filter_by(username = username).first()
        return user
    
    def get_users(self):
        return UserSchema.query.all()

