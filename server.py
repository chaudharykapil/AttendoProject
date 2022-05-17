from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("Home.html")


app.run(debug=True)