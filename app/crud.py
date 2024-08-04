from sqlalchemy.orm import Session
import uuid
from models import User, License


def generate_unique_activation_code(db: Session):
    while True:
        activation_code = str(uuid.uuid4())
        if not db.query(License).filter_by(activation_code=activation_code).first():
            return activation_code


def create_user(db: Session, tarabari_id: str):
    new_user = User(tarabari_id=tarabari_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def create_license(db: Session, tarabari_id: str, additional_days: int):
    activation_code = generate_unique_activation_code(db)
    new_license = License(
        tarabari_id=tarabari_id,
        activation_code=activation_code,
        status='inactive',
        duration=additional_days,
    )
    db.add(new_license)
    db.commit()
    db.refresh(new_license)
    return new_license


def get_user_by_tarabari_id(db: Session, tarabari_id: str):
    return db.query(User).filter_by(tarabari_id=tarabari_id).first()


def get_license_by_activation_code(db: Session, activation_code: str):
    return db.query(License).filter_by(activation_code=activation_code).first()
