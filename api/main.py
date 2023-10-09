import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def send_telegram_message(chat_id, text):
    bot_token = '6032923187:AAGR1u8IcxjPSD7DUZqdaWA9Y-tAPNcnHGs'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, params=params)
    return response.status_code

@app.route('/submit', methods=['POST'])

def submit_form():
    try:
        print(request.form['name'])
        chat_id = '304944970'  
        name = request.form['name']
        phone = request.form['phone']
        code = request.form['code']

        message = f'З сайту!\n\nПацієнт:{name} хочет записаться. Номер телефона: {code + phone}'

        status_code = send_telegram_message(chat_id, message)

        if status_code == 200:
            return 'Данні успішно відправленні в Telegram'
        else:
            return 'Помилка'
    except Exception as e:
        print(str(e))
        return 'Помилка на сервері'
    

@app.route('/submit2', methods=['POST'])
    
def submit_form2():
    chat_id = '304944970'  
    phone = request.form['phone']
    code = request.form['code']

    message = f'З сайту!\n\nПацієнт хочет записаться. Номер телефона:{code + phone}'

    status_code = send_telegram_message(chat_id, message)

    if status_code == 200:
        return 'Данні успішно відправленні в Telegram'
    else:
        return 'Помилка'