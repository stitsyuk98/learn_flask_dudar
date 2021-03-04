from flask import Flask, render_template, url_for


app = Flask(__name__)  # передает данный файл


# отслеживает определенный url адресс
# главная страница
@app.route('/')  # декоратор
@app.route('/home')  # декоратор
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f'It is user page: {name}, {id}'


if __name__ == "__main__":
    app.run(debug=True)  # все ошибки выводятся на страницу
