from flask import Flask, render_template

app = Flask(__name__)
#http://127.0.0.1:8080/index/headname


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)