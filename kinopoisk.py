import requests
import re

new = False
for line in range(25):
    num = line+1
    url = 'https://www.kinopoisk.ru/top/lists/1/filtr/all/sort/order/page/'+str(num)+'/'
    print(url)
    r = requests.get(url)
    with open('kino.txt', 'w') as k:
        k.write(r.text)

    with open('kino.txt', 'r') as f:
        print('go'+str(num))
        for i in f:
            if not '–' in i and not '…' in i
            and not '«' in i and not '»' in i and not '—' in i and not 'Ў' in i: #can be used in WinOS
                if new:
                    new = False
                    print ((re.split(r'"', i))[1])
                if 'data-film-title' in i:
                    print ((re.split(r'"', i))[1])
                    new = True
                    
