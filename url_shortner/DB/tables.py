from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import dotenv_values

from datetime import datetime

config = dotenv_values('config.env')

Base = declarative_base()

engine = create_engine(f"mysql+mysqlconnector://{config['db_user_name']}:{config['db_user_password']}@{config['db_host']}/{config['db_name']}", echo=True)
db_session = Session(bind=engine)


class UrlsCodes(Base):
    __tablename__ = 'urls_codes'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    code = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)