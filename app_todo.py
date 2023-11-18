from flask import Flask, render_template, jsonify, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# start of to-dos --------------------------------------------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///todo.db'
db = SQLAlchemy(app)

# class shoule make table and database

class ToDoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return f'<TodoItem {self.id}>'

@app.route("/")
def home():
    items = ToDoItem.query.all()
    return render_template('index.html',items=items) 

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        if content.strip() != '':
            new_item = ToDoItem(content=content)
            db.session.add(new_item)
            db.session.commit()
        return redirect('/')
    else:
        items = ToDoItem.query.all()
        return render_template('index.html',items=items)

@app.route('/complete/<int:item_id>')
def complete(item_id):
    item = ToDoItem.query.get_or_404(item_id)
    item.completed = True
    db.session.commit()
    return redirect ('/')

@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = ToDoItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect ('/')

# end of to-do -----------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)

