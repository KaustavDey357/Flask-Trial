from flask import Flask , render_template , url_for , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    Task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer , default =0)
    date_created = db.Column(db.DateTime , default=datetime.utcnow())
    
    def _repr_ (self):
        return '<Task %r>' % self.id 


@app.route('/' , methods=['GET','POST'])
def func():
    if(request.method == 'GET'):
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html' , tasks=tasks)
    else : 
        new_content = request.form['content']
        new_task = Todo(Task=new_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "Error!"
        
    
        
if __name__ == "__main__":
    app.run( debug = True)