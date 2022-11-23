from curses import flash
import email
from unicodedata import name
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
# if ENV=='dev':
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:dan@localhost/posts'

db = SQLAlchemy(app)
db.create_all()


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return 'Blog Post' + str(self.id)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return 'Users' + str(self.id)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    return render_template('home.html', posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title,
                            content=post_content,
                            author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_user = Users(name=name,
                         email=email,
                         password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    else:
        all_users = Users.query.order_by(Users.name).all()
        return render_template('home.html', users=all_users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form.get("email")
        passwd = request.form.get("pwd")
        all_users = Users.query.order_by(Users.name).all()
        return render_template('home.html', users=all_users)

    else:
        return render_template('signin.html')


@app.route('/allposts')
def allposts():
    all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    return render_template('allposts.html', posts=all_posts)


@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/')


@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    post = BlogPost.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)