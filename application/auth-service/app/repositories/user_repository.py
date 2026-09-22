from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import hash_password


class UserRepository:

    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(User).filter(
            User.email == email
        ).first()

    @staticmethod
    def create_user(
        db: Session,
        full_name: str,
        email: str,
        password: str,
        role: str
    ):
        user = User(
            full_name=full_name,
            email=email,
            password=hash_password(password),
            role=role
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user