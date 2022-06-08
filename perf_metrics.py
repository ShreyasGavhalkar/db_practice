import pdb
from sqlalchemy import create_engine, Column, Integer, String, Date, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import *
import pprint
Base = declarative_base()

URL = "postgresql://postgres:<your password>@localhost:5432/postgres"

engine = create_engine(URL)


session = sessionmaker(bind=engine)
# pdb.set_trace()
s = session()
q = text("SELECT * FROM pg_stats;")

r = engine.execute(q)
# print(r+"\n\n")all
for row in r:  # this works
    print(row)
    print("\n")
with engine.connect() as con:  # and even this works
    res = con.execute(q)
    print("columns\n")
    pprint.pprint(res.fetchall())
