from flask import Flask , render_template , url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer , default =0)
    date_created = db.Column(db.DateTime , default=datetime.utcnow)


@app.route('/')
def func():
    return render_template('index.html')
if __name__ == "__main__":
    app.run( debug = True)