# necessary imports
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///database.db", echo=False)

Base = declarative_base()


class Insurance(Base):
    __tablename__ = "insurance"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    telephone = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<ID: {self.id}, jmeno: {self.name} {self.lastname}, věk: {self.age}, tel: {self.telephone}>"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
