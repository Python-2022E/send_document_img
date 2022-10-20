import requests
TOKEN = '5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'
chat_id = 5575549228

def send_contact(chat_id,TOKEN):
    url = f'https://api.telegram.org/bot{TOKEN}/sendContact'
    data = {
        'chat_id':chat_id,
        'phone_number':'+998943577744',
        'first_name':"Javohir",
        'last_name':'Jalilov'

    }
    r = requests.post(url,data=data)
    print(r.status_code)


send_contact(chat_id, TOKEN)