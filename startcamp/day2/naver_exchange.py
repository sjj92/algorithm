import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
# print(type(response))

# 3. 받은 응답을 예쁘게 꾸며준다.
data = BeautifulSoup(response, 'html.parser')
# print(data)

# 4. 꾸민 응답중에서 원하는 데이터를 선택.
result = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(result)
