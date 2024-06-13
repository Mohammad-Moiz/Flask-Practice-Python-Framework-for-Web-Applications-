from flask import Blueprint

web = Blueprint("web", __name__)


@web.route('/')
def index():
    return "<h1>Hello World!</h1>"

@web.route('/about')
def about():
    return "<h1>About Page</h1>"

@web.route('/blog/<int:postID>')
def show_blog(postID):
    return f"<h1>Blog Number {postID} </h1>"

