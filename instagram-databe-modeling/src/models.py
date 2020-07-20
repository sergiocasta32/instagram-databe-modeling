import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), index=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), unique=True)
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_tex = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    post = relationship(Post)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

def to_dict(self):
        return {
            'id' : self.id,
            'street_name': self.street_name,
            'street_number' : self.street_number,
            'post_code': self.post_code,
            'email': self.email
        }

render_er(Base, 'diagram.png')