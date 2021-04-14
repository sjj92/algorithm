import requests
from pprint import pprint

KEY = 'dH%2BRNa%2Fg8eT3FybEgXGijD54sjaPN5FZOkRKD3EhCwBxDFJFYS4qfIbxlV9p6O9f%2B5lxy0YHC7%2Fj0NVksLv5OA%3D%3D'
return_type = 'json'
num_of_rows = '5'
page_no = '1'
sido_Name = '서울'
ver = '1.0'


url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sido_Name}&ver={ver}'

response = requests.get(url).json()
# print(response)

# sidoname의 미세먼지 농도는 pm10value입니다. 라는 메세지를 출력하세요.


station_Name = response['response']['body']['items'][0]['stationName']
dust = response['response']['body']['items'][0]['pm10Grade']


import requests

TOKEN = '1511510793:AAGfhHQIopVb2d3r8mkO2FSA_YgrU3amQj8'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

# chat_id 받기 (getupdates)
update_url = f'{APP_URL}/getupdates'
response = requests.get(update_url).json()
# print(response)

# 3. chat_id 찾기
chat_id = response.get('result')[0].get('message').get('from').get('id')
# print(chat_id)

# 4. message 보내기 (sendMessage)
text = f'{station_Name}의 미세먼지 농도는 pm {dust}value입니다.'
message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url) # 메세지 보내달라고 요청하기


