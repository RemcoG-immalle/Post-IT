from flask import Flask,request, redirect, url_for
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
    return redirect(url_for('static', filename='index.html'))

#@app.route("/Register")
#def Authenticate():
#    username = request.args.get('Name')
#    password = request.args.get('Password')
#    cursor = mysql.connect().cursor()
#    cursor.execute("SELECT * from Users where Name='" + username + "' and Password='" + password + "'")
#    data = cursor.fetchone()
#    if data is None:
#     return "Username or Password is wrong"
#    else:
#     return "Logged in successfully"

if __name__ == "__main__":
    app.run()
