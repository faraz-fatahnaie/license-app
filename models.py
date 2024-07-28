# models.py
from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "postgresql://postgres:1234@localhost/license_db"  # Replace with your actual PostgreSQL URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, index=True)
    tarabari_id = Column(String(80), unique=True, nullable=False, index=True)
    name = Column(String(120))
    email = Column(String(120))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class License(Base):
    __tablename__ = 'license'
    license_id = Column(Integer, primary_key=True, index=True)
    tarabari_id = Column(String(80), ForeignKey('user.tarabari_id'), nullable=False)
    activation_code = Column(String(80), unique=True, nullable=False, index=True)
    status = Column(String(20), default='inactive')
    activate_date = Column(DateTime)
    duration = Column(Integer, nullable=False)
    validation_count = Column(Integer, default=0)
    expiry_date = Column(DateTime, nullable=True)
    hardware_unique_id = Column(String(120), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

Base.metadata.create_all(bind=engine)
