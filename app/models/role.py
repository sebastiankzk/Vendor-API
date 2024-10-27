from sqlalchemy import Column, Integer, String
from app.models import Base

class Role(Base):
    __tablename__ = 'ROLE'

    roleID = Column(Integer, primary_key=True)
    roleName = Column(String(50), nullable=False)