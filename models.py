from sqlalchemy import Column, ForeignKey, Enum, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, Session

from database import engine

Base = declarative_base()


class Tree(Base):
    __tablename__ = 'tree'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def get_entries(self, db: Session, table: Base):
        return db.query(table).filter_by(tree_id=self.id)


class Pair(Base):
    __tablename__ = 'pair'

    id = Column(Integer, primary_key=True)
    tree_id = Column(Integer, ForeignKey('tree.id'))
    husband_id = Column(Integer, ForeignKey('person.id'))
    wife_id = Column(Integer, ForeignKey('person.id'))
    wedding_date = Column(String)


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    tree_id = Column(Integer, ForeignKey('tree.id'))
    pair_id = Column(Integer, ForeignKey('pair.id'))
    name = Column(String)
    bio = Column(String)
    gender = Column(Enum('m', 'f'))
    alive = Column(Boolean)
    birth_date = Column(String)
    death_date = Column(String)


Base.metadata.create_all(engine)
