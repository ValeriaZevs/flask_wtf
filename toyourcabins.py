from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
#http://127.0.0.1:8080/distribution


@app.route('/distribution')
def distribution():
    params = ['Уилл Смитт', 'Анджелина Джоли', 'Том Холланд', 'Фрэнк Синатра', 'Джони Депп']
    return render_template('toyourcabins.html', params=params)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)