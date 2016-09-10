#!/usr/bin/python
# -*- coding: utf-8 -*-


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Declare a Mapping
Base = declarative_base()
engine = None


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String(20))

    def __repr__(self):
        return "<User(username'%s', password='%s')>" % (self.username, self.password)


# Create a new Engine instance
# URL = dialect[+driver]://user:password@host/dbname[?key=value..]
# dialect = mysql/oracle/postgresql
# driver = mysqlconnector/mysqldb
#
# sqlite://<nohostname>/<path>
# engine = create_engine('sqlite:///foo.db')
def setup_database(echo=True):
    global engine
    url = 'mysql+mysqlconnector://root:root@42@localhost:3306/alchemy'
    engine = create_engine(url, echo=echo)
    Base.metadata.drop_all(engine)      # drop tables
    Base.metadata.create_all(engine)    # create tables

    # Session = sessionmaker(bind=engine)


def update(_user):
    session = Session(bind=engine)
    session.query(User).filter(User.username == _user.username).update({User.password: _user.password})
    session.commit()                    # write changes to the database
    session.close()


def insert(_users):
    session = Session(bind=engine)      # create session
    session.add_all(_users)
    session.commit()
    session.close()


def delete(_username):
    session = Session(bind=engine)
    session.query(User).filter(User.username == _username).delete()
    session.commit()                    # write changes to the database
    session.close()


def find(_username):
    session = Session(bind=engine)      # create session
    _user = session.query(User).filter(User.username == _username).one()
    session.close()
    return _user


def findall():
    session = Session(bind=engine)      # create session
    _users = session.query(User).all()
    session.close()
    return _users


if __name__ == '__main__':
    setup_database()
    user = User(username='colorus', password='colorus@74')
    user2 = User(username='metry', password='metry@53')
    user3 = User(username='admin', password='admin@53')
    users = [user, user2]
    insert(users)
    user = find('colorus')
    print('user: ', user)
    delete('colorus')
    print('delete colorus...')
    users = findall()
    print('users: ', users)
    user = User(username='metry', password='metry@5')
    update(user)
    print('update metry...')
    users = findall()
    print('users: ', users)









