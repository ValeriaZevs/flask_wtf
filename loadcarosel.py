from flask import Flask, render_template, request
from PIL import Image
import io
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
#http://127.0.0.1:8080/loadcarosel


photos = ['static/img/one.jpg', 'static/img/two.jpg']


@app.route('/loadcarosel')
def loadcarosel():
    global photos
    if request.method == 'GET':
        return render_template('loadcarosel.html', photos=photos, length=len(photos))
    elif request.method == 'POST':
        f = request.files['file'].read()

        img = Image.new('RGB', (200, 200), 'black')
        img.save(f'test{len(photos)}.jpg')
        photos.append(f'static/img/test{len(photos)}.jpg')

        io_bytes = io.BytesIO(f)
        img = Image.open(io_bytes)
        img.save(f'test{len(photos)}.jpg')
        return render_template('loadcarosel.html', photos=photos, length=len(photos))



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)