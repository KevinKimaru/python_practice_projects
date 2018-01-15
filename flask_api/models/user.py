import uuid

import datetime
from flask import session

from common.database import Database
from models.blog import Blog


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one(collection="users", query={"email" : email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one(collection="users", query={"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            return  user.password == password
        return False

    @staticmethod
    def register(email, password):
        user = User.get_by_email(email)
        if user == None:
            #user doesnt exist so we can create one
            new_user = User(email, password)
            new_user.save_to_mongo()
            session["email"]  = email
            return True
        else:
            #user exists
            return False

    @staticmethod
    def login(user_email):
        session["email"] = user_email

    @staticmethod
    def logout():
        session["email"] = None

    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def new_blog(self, title, description):
        blog = Blog(
            author=self.email,
            author_id=self._id,
            title=title,
            description=description,
        )
        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id, title, content, date=datetime.datetime.utcnow()):
        blog = Blog.from_mongo(blog_id)
        blog.new_post(
            title=title,
            content=content,
            date=date
        )

    def json(self):
        return {
            "email" : self.email,
            "password" : self.password,
            "_id" : self._id
        }

    def save_to_mongo(self):
        Database.insert("users", self.json())