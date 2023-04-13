from flask import Flask, render_template

app = Flask(__name__)
#http://127.0.0.1:8080/index/headname
#http://127.0.0.1:8080/training/инженер
#http://127.0.0.1:8080/odd_even


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('prof.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)