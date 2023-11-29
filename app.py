from flask import * # Импорт всего пакета flask
app = Flask(__name__)  # Создание экземпляра приложения Flask

# Определение маршрута для главной страницы
@app.route('/')
def index():
    return render_template('index.html')  # Возврат шаблона index.html

# Определение маршрута для страницы контактов
@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')  # Возврат шаблона contacts.html

# Проверка, является ли файл, в котором выполняется данный код, главным
if __name__ == "__main__":
     app.run()  # Запуск приложения
