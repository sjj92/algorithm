import requests
from bs4 import BeautifulSoup

KEY = 'HnojHK%2BBftAEynpyD0N3n0qhgheAi02RQAfRblaqWLGk4SV%2B1vq6oPGq5Ve7BPvlLVGsPI7QY%2BMZ30eziih8pg%3D%3D'
URL = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=5&pageNo=1&sidoName=서울&ver=1.0&returnType=xml'

response = requests.get(URL).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[0]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')


# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.

if dust > 150:
    print("매우나쁨")
elif 150 >= dust > 80:
    print("나쁨")
elif 80 >= dust > 30:
    print("보통")
else:
    print("좋음")

