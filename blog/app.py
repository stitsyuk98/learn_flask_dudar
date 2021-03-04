from flask import Flask


app = Flask(__name__)  # передает данный файл


# отслеживает определенный url адресс
# главная страница
@app.route('/')  # декоратор
def index():
    return 'It is index page'


@app.route('/about')
def about():
    return 'It is about page'


if __name__ == "__main__":
    app.run(debug=True)  # все ошибки выводятся на страницу
