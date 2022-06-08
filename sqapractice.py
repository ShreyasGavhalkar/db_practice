from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, create_engine

Base = declarative_base()


# goes into config.py
DATABASE_URI = 'postgresql+psycopg2://postgres:AcessPassword@localhost:5432/books'

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)


class Book(Base):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)

    def __repr__(self):
        return "<Book(title='{}', author='{}', pages='{}', published='{}')".format(self.title, self.author, self.pages, self.published)
