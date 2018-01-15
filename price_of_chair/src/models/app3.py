from src.database import Database
from src.menu import Menu
from src.models.blog import Blog
from src.models.post import Post

Database.initialize()

# post = Post(blog_id="123", title="Another awesome post", content="Content sample")
#
# Post.save_to_mongo()
#
# post = post.from_mongo(id="")
# print(post)
#
# posts = Post.from_blog("123")
# for post in posts:
#     print(post)


# blog = Blog(
#     author="Kevin",
#     title="Sample title",
#     description="Sample description"
# )
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.from_mongo(blog.id)
#
# print(blog.get_posts())

menu = Menu()
menu.run_menu()