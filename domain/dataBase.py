from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime

Base = declarative_base()


class MyWarning(Base):
    __tablename__ = 'warning'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    date_time = Column(DateTime, nullable=False)
    port = Column(Integer, nullable=False)
    answer_time = Column(Integer, nullable=False)

    def __str__(self):
        return "id: {}||date_time: {}|| port: {}|| answer_time: {}"\
            .format(self.id, self.date_time, self.port, self.answer_time)
