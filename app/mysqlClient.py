from app.models.user import User
from db import db

class Client:

    def add(self, name):
        prevUser = User.query.order_by(User.id.desc()).first()

        id = prevUser.id + 1 if prevUser is not None else 1
        user = User(id, name)

        db.session.add(user)
        db.session.commit()

    def all(self):
        return User.query.order_by(User.id.desc()).all()
