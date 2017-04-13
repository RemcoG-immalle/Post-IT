from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/<wall>')
def hello(wall=None):
    return render_template('wall.html', wall=wall)

if __name__ == "__main__":
    app.run()
