from flask import Flask
from app.blueprints import web, user
from app.extensions import db

print("name: " , __name__)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


db.init_app(app)
app.register_blueprint(web.web)
app.register_blueprint(user.user)

with app.app_context():
    db.create_all()




if __name__ == '__main__':
    app.run(debug=True)