from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///./saharaProduct.db',connect_args = {"check_same_thread":False})

Sessionlocal = sessionmaker(autocommit = False,autoflush = False,bind = engine)
Base = declarative_base()