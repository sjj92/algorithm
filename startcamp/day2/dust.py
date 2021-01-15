import requests
from pprint import pprint

key = 'dH%2BRNa%2Fg8eT3FybEgXGijD54sjaPN5FZOkRKD3EhCwBxDFJFYS4qfIbxlV9p6O9f%2B5lxy0YHC7%2Fj0NVksLv5OA%3D%3D'
return_type = 'json'
num_of_rows = '5'
page_no = '1'
sido_Name = '서울'
ver = '1.0'


url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sido_Name}&ver={ver}'

response = requests.get(url).json()
# print(response)

# sidoname의 미세먼지 농도는 pm10value입니다. 라는 메세지를 출력하세요.


station_Name = response['response']['body']['items'][0]['stationName']
dust = response['response']['body']['items'][0]['pm10Grade']

print(f'{station_Name}의 미세먼지 농도는 pm {dust}value입니다.')

