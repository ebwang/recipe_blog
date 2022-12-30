from flask import Blueprint, render_template, redirect, url_for, current_app, request # New imports added
from sqlmodel import Session, select
from models.post import Post

post_pages = Blueprint("posts", __name__)


@post_pages.get("/post/<string:title>")
def display_post(title: str):
    with Session(current_app.engine) as session:
        statement = select(Post).where(Post.title == title)
        post = session.exec(statement).first()
        return render_template("post.html", title=title, content=post.content)

@post_pages.route("/post/", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        with Session(current_app.engine) as session:
            session.add(Post(title=title, content=content))
            session.commit()
        return redirect(url_for("posts.display_post", title=title))
    return render_template("new_post.html")