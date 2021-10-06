from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask("Deployment")
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydb/database.sqlite'

db = SQLAlchemy(app)

class IIEC(db.Model):
    ids = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    gender = db.Column(db.Text)

    def __init__(self,name,age,gender):
       self.name=name
       self.age=age
       self.gender = gender

db.create_all()


@app.route('/create',methods=['GET'])
def create():
    data=render_template("create.html")
    return data

@app.route('/createoutput',methods=['GET'])
def crateout():
    name1 = request.args.get("n")
    age1 = request.args.get("a")
    gender1 = request.args.get("g")
    cr = IIEC(name1,age1,gender1)
    db.session.add(cr)
    db.session.commit()
    return "added" 

@app.route('/read',methods=['GET'])
def read():
    data=render_template("read.html")
    return data

@app.route('/readoutput',methods=['GET'])
def readout():
    data=render_template("read.html")
    output = request.args.get("i")
    a = int(output)
    store = IIEC.query.get(a)
    print(store.name)
    return '{} {} {}'.format(store.name, store.age, store.gender)


@app.route('/delete',methods=['GET'])
def update():
    data=render_template("delete.html")
    return data

@app.route('/deleteoutput',methods=['GET'])
def updateout():
    data=render_template("delete.html")
    output = request.args.get("i")
    a = int(output)
    store = IIEC.query.get(a)
    db.session.delete(store)
    db.session.commit()
    print(store.name)
    return 'Value deleted , for check enter same id again in form'


