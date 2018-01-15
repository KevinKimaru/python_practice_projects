import uuid
import datetime

from common.database import Database
from models.post import Post


class Blog(object):
    def __init__(self, author, author_id, title, description, _id=None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        post = Post(
            blog_id=self._id,
            title=title,
            content=content,
            author=self.author,
            creation_date=date
        )
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(
            collection='blogs',
            data=self.json()
        )
    def json(self):
        return {
            '_id' : self._id,
            'author' : self.author,
            'author_id' : self.author_id,
            'description' : self.description,
            'title' : self.title,
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection="blogs", query={'_id' : id})
        # return cls(
        #     author=blog_data['author'],
        #     title=blog_data['title'],
        #     description=blog_data['description'],
        #     id=blog_data['_id']
        # )
        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls, author_id):
        blogs = Database.find(collection="blogs",
                              query={"author_id" : author_id})
        return [cls(**blog) for blog in blogs]

