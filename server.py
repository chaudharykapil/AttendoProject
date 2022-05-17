from flask import Flask, redirect,render_template,abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import nullslast


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:kapil@localhost/attendo"
db = SQLAlchemy(app=app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True,nullable = False)
    name = db.Column(db.String(50),nullable = False)
    clg_id = db.Column(db.String(50),nullable = False)
    email = db.Column(db.String(50),nullable = False)
    password = db.Column(db.String(100),nullable=False)


class UserDetail(db.Model):
    __tablename__ = "userdetail"
    id = db.Column(db.Integer,primary_key = True,nullable = False)
    user_id = db.Column(db.Integer,nullable = False)
    ct1_date = db.Column(db.String(10),nullable = True)
    c12_date = db.Column(db.String(10),nullable = True)
    pue_date = db.Column(db.String(10),nullable= True)
    total_att = db.Column(db.Integer,nullable = True)


@app.route("/")
def Home():
    return render_template("Home.html")
@app.route("/register",method = ["POST"])
def Register():
    return redirect("/login")
@app.route("/login",method = ["POST","GET"])
def Login():
    return render_template("login.html")
@app.route("/calendar")
def Calendar():
    pass
@app.route("/setting")
def Setting():
    pass
@app.route("/time-table")
def TimeTable():
    pass
@app.route("/attendence")
def Attendence():
    pass

app.run(debug=True)