Веб-приложение, в основе которого лежит фреймворк Fastapi и база данных Tinydb.
Приложение получает на вход поля формы в теле POST запроса, на выходе возвращается имя наиболее подходящей формы.
Дополнительно - для удобства просмотра реализован GET метод для получения всех известных форм.
Информация по запуску приложения: необходимо скачать репозиторий github. Это возможно сделать посредством команды в терминале IDE-программы(напрмер PyCharm): git clone https://github.com/AeonaNova/Form_database_app.git
после того, как проект загружен и открыт в IDE, необходимо создать виртуальное окружение - в случае Windows команда в терминале python -m venv venv, активировать его venv\scripts\activate
Затем установить зависимости для работы с проектом командой в терминале pip install > requirements.txt
После этого возможен запуск приложения командой в терминале uvicorn main:app --reload, открыть в браузере адрес http://127.0.0.1:8000/docs
Приложение может быть размещено в docker-образ.
Для случая Windows потребуется docker desktop программа в запущенном состоянии и включенным в разделе настроек general параметром Use the WSL 2 based engine.
Для запуска приложения посредством docker потребуется выполнить команды в терминале docker build -t form-database .
И затем docker run -p 80:80 form-database
После этого открыть в браузере адрес http://127.0.0.1:80/docs
