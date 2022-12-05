import sqlalchemy as db
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class mysqllib:
    def __init__(self, host, port, user, password, database):
        if not password:
            password = ""

        self.engine = db.create_engine("mysql+pymysql://{}:{}@{}:{}/{}"
                                       .format(user, password,
                                               host, port, database))

        self.meta = db.MetaData()
        print("Connected to mysql")

    """get from database"""
    def getLogs(self, model: Base):
        session = Session(self.engine)
        try:
            rows = session.query(model)
            return rows
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()
