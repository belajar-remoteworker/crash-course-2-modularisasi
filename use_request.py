import requests

url = 'https://detik.com'
try :
    response = requests.get(url)
    print(f'Sukses {response}')
    print(f'content {response.text}')
except Exception :
    print('There is an error')
print('Program ended')



