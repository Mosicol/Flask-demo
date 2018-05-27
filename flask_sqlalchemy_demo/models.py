

from sqlalchemy import Column,Integer,String,create_engine
from  sqlalchemy.ext.declarative import declarative_base

DB_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/alembic_demo?charset=utf8"

engine = create_engine(DB_URI)

Base = declarative_base(engine)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)




