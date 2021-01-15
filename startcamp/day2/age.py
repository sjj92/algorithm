import requests

name = 'harry'
url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json()
# print(type(response))

age = response['age']

print(f'{name}의 나이는 {age}살 입니다.')

