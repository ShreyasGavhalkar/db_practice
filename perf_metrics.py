import pdb
from sqlalchemy import create_engine, Column, Integer, String, Date, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import *
import pprint
Base = declarative_base()

URL = "postgresql://postgres:AcessPassword@localhost:5432/postgres"

engine = create_engine(URL)


session = sessionmaker(bind=engine)
# pdb.set_trace()

q = text("SELECT * FROM pg_stat_activity;")

r = engine.execute(q)
print(r)
# postgres=# SELECT * FROM pg_stat_activity;
