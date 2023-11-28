from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable= False)
    desc = db.Column(db.String(500),nullable = False)
    time = db.Column(db.DateTime,default = datetime.utcnow)


    def __repr__(self):
        return f"{self.sno}-{self.title}"

@app.route('/',methods = ['GET','POST'])
def hello():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title = title,desc = desc)
        db.session.add(todo)
        db.session.commit()


    todo = Todo.query.all()
    return render_template('index.html',todo = todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    item = Todo.query.filter_by(sno=sno).first()
    db.session.delete(item)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>',methods =['GET','POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.commit()
        return redirect('/')
    item = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo = item)


@app.route('/create_tables')
def create_tables():
    with app.app_context():
        db.create_all()
    return 'Tables created successfully!'


@app.route('/search', methods = ['GET','POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        # Assuming you have a 'title' field in your Todo model
        print(search_term)
        results = Todo.query.filter(Todo.title.ilike(f"%{search_term}%")).all()
        print(results)
        return render_template('search.html', results=results, search_term=search_term)

    return redirect('/')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)