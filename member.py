from flask import Flask, render_template, request
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
#http://127.0.0.1:8080/member

@app.route('/member')
def member():
    with open("templates/member.json", "r") as fh:
        r = json.load(fh)
        return render_template('member.html', sp=r['members'])





if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)