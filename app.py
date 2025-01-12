from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/social_media_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Post model
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

# Create tables if they don't exist
@app.before_first_request
def create_tables():
    db.create_all()

# Homepage: Show all posts and a form to create a new post
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            new_post = Post(content=content)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('index'))
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
