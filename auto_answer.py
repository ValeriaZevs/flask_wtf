from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
#http://127.0.0.1:8080/auto_answer


@app.route('/answer')
def answer():
    params = dict()
    params['title'] = 'Обычный ответ'
    return render_template('auto_answer.html', params=params)


@app.route('/auto_answer')
def auto_answer():
    params = dict()
    params['title'] = 'Автоматический ответ'
    params['Фамилия'] = 'Зизевских'
    params['Имя'] = 'Валерия'
    params['Образование'] = 'Высшее'
    params['Профессия'] = 'Программист-разработчик'
    params['Пол'] = 'Женский'
    params['Мотивация'] = 'Вперед в будущее!'
    params['Готовность остаться на Марсе'] = True
    return render_template('auto_answer.html', params=params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)