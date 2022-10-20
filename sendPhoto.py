import requests
TOKEN = '5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'
r = requests.get('https://dog.ceo/api/breeds/image/random')

chat_id = 5575549228

data = r.json()
img_url = data.get('message')

url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
data = {
    'chat_id':chat_id,
    'photo':img_url

}
r = requests.post(url,data=data)
print(r.status_code)