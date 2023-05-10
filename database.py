from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('sqlite:///data.db')
SessionLocal = sessionmaker(bind=engine)
db: Session = SessionLocal()
