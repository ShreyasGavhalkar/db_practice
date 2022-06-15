from jinja2 import Template
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, inspect, Table
import webbrowser

Base = declarative_base()
db_name = input("Enter database name: ")
password = input("Enter password: ")

url = "postgresql://postgres:"+password+"@localhost:5432/"+db_name

engine = create_engine(url)
metadata_obj = MetaData(bind=engine)

insp = inspect(engine)
schemas = insp.get_schema_names()
tbls = insp.get_table_names(schema='public')
with open("templates/new_jinja_template.html.jinja") as f:
    tmplt = Template(f.read())
of = tmplt.render(tables=tbls)


with open("templates/tables_template.html.jinja") as f:
    t = Template(f.read())
    for i in tbls:
        cols = insp.get_columns(i)
        out = t.render(table=i, cols=cols)
        with open("output_pages/{}.html".format(i), "w") as o:
            o.write(out)
        tb=Table(i, metadata_obj, autoload=True, autoload_with=engine)
        primary_key=tb.primary_key.columns.values()
        # print(primary_key)
        for j in primary_key:
            print(j.name, end=' ')
        print()


with open("output_pages/output.html", "w") as f:
    f.write(of)
    webbrowser.open("output_pages/output.html")
