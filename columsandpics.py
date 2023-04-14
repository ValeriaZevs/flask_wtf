from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
#http://127.0.0.1:8080/table/female/25


@app.route('/table/<sex>/<age>')
def distribution(sex, age):
    return render_template('columsandpics.html', sex=sex, age=int(age))



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)