from sqlalchemy.exc import IntegrityError

from backend.db import db_session
from backend.errors import ConflictError, NotFoundError
from backend.models import User


class UserRepo:
    name = 'user'

    def add(self, username: str) -> User:
        try:
            new_user = User(username=username)
            db_session.add(new_user)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)
        return new_user

    def get_all(self) -> list[User]:
        return User.query.all()

    def get_by_id(self, uid: int) -> User:
        user = User.query.filter(User.uid == uid).first()
        if not user:
            raise NotFoundError(self.name)
        return user

    def update(self, uid: int, new_name: str) -> User:
        user = User.query.filter(User.uid == uid).first()
        if not user:
            raise NotFoundError(self.name)
        try:
            user.username = new_name
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)
        return user

    def delete(self, uid: int) -> None:
        user = User.query.filter(User.uid == uid).first()
        if not user:
            raise NotFoundError(self.name)
        db_session.delete(user)
        db_session.commit()

    def add_users(self, planning_id: int, name: str) -> User:
        try:
            new_user = User(name=name, planning_id=planning_id)
            db_session.add(new_user)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)
        return new_user

    def get_all_users(self, planning_id: int) -> list[User]:
        users = User.query.filter(User.planning_id == planning_id)
        return users

    def get_user_by_id(self, planning_id: int, user_id: int) -> User:
        user = User.query.filter(
            User.planning_id == planning_id,
            User.uid == user_id
        ).first()
        if not user:
            raise NotFoundError(self.name)
        return user
