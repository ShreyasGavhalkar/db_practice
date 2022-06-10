
from sqlalchemy import create_engine, Column, Integer, String, Date, Table, MetaData, or_, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
# from sqlalchemy import *
from sqlalchemy.dialects.postgresql import MONEY
import datetime
import pprint

Base = declarative_base()


class books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    bookname = Column(String)


class table1(Base):
    __tablename__ = 'table1'
    id = Column(Integer, primary_key=True)
    f_name = Column(String)
    l_name = Column(String)
    price = Column(MONEY)


class table2(Base):
    __tablename__ = 'table2'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)

    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>".format(self.title, self.author, self.pages, self.published)


def get_engine(user, password, host, port, db):
    url = "postgresql://"+user+":"+password+"@"+host+":"+port+"/"+db
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50)
    return engine


def get_session(engine):
    session = sessionmaker(bind=engine)
    return session


psswd = input("Enter password\n")
engine = get_engine("postgres", psswd,
                    "localhost", "5432", "test1")

session = get_session(engine)
print(session)


metadata_obj = MetaData(bind=engine)
Base.metadata.create_all(engine)
s1 = session()
obj = table2(
    title='just a test title',
    author='test author',
    pages=500,
    published=datetime.datetime.now()
)
# s1.add(obj)
# s1.commit()
s1.close()
l1 = [table2(
    title="An Introduction to Statistical Learning: with Applications in R",
    author="Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani",
    pages=426,
    published=datetime.datetime(2013, 1, 1)),
    table2(title="The Elements of Statistical Learning: Data Mining, Inference and Prediction",
           author="Trevor Hastie, Robert Tibshirani, Jerome Friedman",
           pages=745,
           published=datetime.datetime(2009, 1, 1)),
    table2(title="Pattern Recognition and Machine Learning",
           author="Christopher Bishop",
           pages=738,
           published=datetime.datetime(2004, 6, 4)),
    table2(title="Machine Learning: A Probabilistic Perspective",
           author="Kevin Murphy",
           pages=1104,
           published=datetime.datetime(2012, 8, 4)),
    table2(title="Deep Learning",
           author="Ian Goodfellow, Yoshua Bengio, Aaron Courville, Francis Bach",
           pages=775,
           published=datetime.datetime(2016, 10, 8))

]
s = session()
# for data in l1:
#     s.add(data)
# s.commit()
pprint.pprint(s.query(table2).all())
print("\n\n\n")
pprint.pprint(s.query(table2).filter(or_(table2.pages > 700,
              table2.published > datetime.datetime(2016, 1, 1))).order_by(table2.id.desc()).all())

# q = text("DELETE FROM table2 WHERE id='1'")
# engine.execute(q)
# engine.execute(delete(table2).where(table2.id == 4))
s.close()
# print("\n\nprinting tables")
# tables = metadata_obj.tables.keys()
# print(tables)
