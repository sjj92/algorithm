import requests


token = '1511510793:AAGfhHQIopVb2d3r8mkO2FSA_YgrU3amQj8'
app_url = f'https://api.telegram.org/bot{token}'

# chat_id 받기 (getupdates)
update_url = f'{app_url}/getupdates'
response = requests.get(update_url).json()
# print(response)

# 3. chat_id 찾기
chat_id = response.get('result')[0].get('message').get('from').get('id')
# print(chat_id)

# 4. message 보내기 (sendMessage)
text = '방가방가'
message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url) # 메세지 보내달라고 요청하기

