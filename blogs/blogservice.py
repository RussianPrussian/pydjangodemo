import blogs.models as blog
import datetime


def add_blog(blog_text):
    print(blog_text)
    new_post = blog.Post(post_text=blog_text, author='Alex', pub_date=datetime.datetime.now())
    new_post.save()



