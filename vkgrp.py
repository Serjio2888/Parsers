import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType


session = requests.Session()
login, password = 'vk.login', 'vk.pass'
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
    
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
print('working')

t = vk.users.search(
    sort=0,count=1000,city=119,country=1,
    group_id=146657779, has_photo=1, age_to=21, age_from=18,
                    )#см vk.com/dev/ раздел Users
a = list()
print(t['items'][0]['id'])
for i in t['items']:
    a.append('vk.com/id'+str(i['id']))


new = '\n'.join(a)

with open('ids.txt', 'w') as lol:
    lol.write(new)

