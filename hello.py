from flask import Flask,request, redirect, url_for, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'post_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'imma'
app.config['MYSQL_DATABASE_DB'] = 'Post_IT'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
@app.route("/home")
@app.route("/Home")
def hello():
    return render_template("home.html")

@app.route("/Wall")
def Authenticate():
    wallname = request.args.get('Name')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM Walls where wall_name='" + wallname + "'")
    data = cursor.fetchone()
    if data is None:
     return "No Wall with this name found."
    else:
     return "Found wall and connected."
     # return render_template("wall.html")

if __name__ == "__main__":
    app.run()
