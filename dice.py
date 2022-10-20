import requests
TOKEN = '5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'
chat_id = 5575549228

def send_dice(chat_id,TOKEN):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDice'
    data = {
        'chat_id':chat_id,
        'emoji':'🎰'

    }
    r = requests.post(url,data=data)
    print(r.status_code)


send_dice(chat_id, TOKEN)