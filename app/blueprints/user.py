from flask import Blueprint, request, render_template, url_for, redirect
from app.user import User
from app.extensions import db

user = Blueprint("user", __name__)


@user.route('/user/', methods=["GET"])
def index(name=None):
         users = User.query.all()
         return render_template("user/index.html", name=name, users=users)

    
@user.route('/user/', methods=["POST"])
def store():
        new_user = User(
              name = request.form["name"],
              email = request.form["email"]
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("user.index"))


@user.route("/user/create", methods=["GET"])
def create():
     return render_template("user/create.html")

    
@user.route('/user/<int:id>', methods=["DELETE", "POST"])
def user_id(id):
    if request.method == "PUT":
            return "<h1>Update User!</h1>"
    elif request.method == "DELETE":
         return "<h1>Delete User!</h1>"


@user.route('/user/<id>')
def about_Username(id=None):
    return render_template("user/show.html", id=id)