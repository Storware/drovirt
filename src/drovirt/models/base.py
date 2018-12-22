from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = None
Base = declarative_base()
DBSession = scoped_session(sessionmaker())

