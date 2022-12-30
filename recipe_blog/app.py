from flask import Flask
from routes.post import post_pages
from sqlmodel import SQLModel, create_engine
from models.post import Post

def app():
    app = Flask(__name__)
    app.engine = create_engine("sqlite:///recipe_blog.db")
    SQLModel.metadata.create_all(app.engine)
    app.register_blueprint(post_pages)
    app.run(debug=True)

    return app
if __name__ == '__main__':
    app()
