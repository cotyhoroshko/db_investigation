from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import create_engine, MetaData, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.environ['DATABASE_URL'])
metadata = MetaData()
Base = declarative_base(metadata)
Session = sessionmaker(bind=engine)


class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    url = Column(String())
    result_all = Column(JSON)
    result_no_stop_words = Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)
