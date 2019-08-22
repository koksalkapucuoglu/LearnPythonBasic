from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/maxwera/Desktop/TodoApp/todo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html",todos = todos)

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    """if todo.complete == True:
        todo.complete = False
    else:
        todo.complete = True"""
    todo.complete = not todo.complete   
    
    db.session.commit()
    
    return redirect(url_for("index"))

@app.route("/add",methods =["POST"]) #sadece post request edildiğinde buraya girsin
def addTodo():
    title = request.form.get("title")#form input kısmına name = title eklemiştik. buradaki veriyi almak için bu filtrelemeyi kullanıyoruz
    newTodo = Todo(title = title,complete = False) #db başlıklarını ve girdileri kolay girmek amacıyla oluşturduğumuz Todo() classına title ve complete verilerini yolluyoruz. burada compelte ilk başta false olacak
    db.session.add(newTodo)#orm'de veri tabanına ekleme komutu
    db.session.commit()#değişiklik yaptığımız için commit yapmak gerekiyor
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)#primary key olsun ve auto increment olsun
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


if __name__   == "__main__":
    db.create_all()#buradaki tüm classları bir tablo olarak databaseye ekle,oluşturulmuş tabloları ise bir daha oluşturmaz.
    app.run(debug=True)

