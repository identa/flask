from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint, create_engine
from sqlalchemy.sql import select
from create import app, jsonify
engine = create_engine("mysql://root:root@localhost/spring", echo=True)
metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(45)),
              Column('fullname', String(45)))

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String(100), nullable=False))


metadata.create_all(engine)
conn = engine.connect()



@app.route('/connect')
def connect():
    # The echo flag is a shortcut to setting up SQLAlchemy logging, which is accomplished via Python’s standard logging module.
    # With it enabled, we’ll see all the generated SQL produced.
    # If you are working through this tutorial and want less output generated, set it to False.
    # This tutorial will format the SQL behind a popup window so it doesn’t get in our way; just click the “SQL” links to see what’s being generated.
    # engine = create_engine('mysql://root:root@localhost/spring', echo=True)


    # Return a new Connection object.
    # The Connection object is a facade that uses a DBAPI connection internally in order to communicate with the database.
    # This connection is procured from the connection-holding Pool referenced by this Engine.
    # When the close() method of the Connection object is called, the underlying DBAPI connection is then returned to the connection pool, where it may be used again in a subsequent call to connect().
    # conn = engine.connect()
    results = conn.execute('select destination, origin from flights')
    resp = jsonify(
        {
            'result': [dict(result) for result in results]
        }
    )
    return resp



@app.route('/insert_origin')
def origin_insert():
    ins = users.insert().values(name="jack", fullname="Jack Jones")
    print(str(ins))
    conn.execute(ins)
    return "a"


@app.route('/getall')
def getall():
    list = select([users])
    result = conn.execute(list)
    for row in result:
        print(dict(row))
    return "b"
