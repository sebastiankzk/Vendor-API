from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.models.role import Role
from app.models import Base

class User(Base):
    __tablename__ = 'USER'

    userID = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    userPassword = Column(String(255), nullable=False)
    roleID = Column(Integer, nullable=False)
    isDisabled = Column(Boolean, nullable=False)