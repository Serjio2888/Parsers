#import requests
import re

new = False

with open('kino.txt', 'r') as f:#подразумевает, что уже был использован kinopoisk.py
    print('go')
    strings = 0
    for i in f:
        if not '–' in i and not '…' in i and not '«' in i and not '»' in i and not '—' in i and not 'Ў' in i:#for Win
            if new:
                new = False
                print ((re.split(r'"', i))[1])
            if 'font-weight: bold" href="/film/' in i:
                strings = 0
                line=((re.split(r'"', i)))
                strings+=6
                for k in line:
                    if re.findall(r'>*</a><span style=', k):
                        n = re.findall(r'[А-я]+', k)
                        l = ' '
                        print('!!!!   ',l.join(n), '    !!!!')
                        
                    if re.findall(r'<nobr>', k):
                        
                        n = re.findall(r'[0-9]+', k)
                        for i in n:
                            if len(i)==4:
                                print('Год:', i)
                            if len(i)==2 or len(i)==3:
                                print('Длительность:' , i, 'минут')

                        
            else:
                if strings==1:
                    #print(i)
                    n = re.findall(r'[[А-я]+', i)
                    if n:
                        print('В главных ролях:', ' '.join(n))#надо поправить - разделять запятыми актеров
                    print('-----------------------------------')
                if strings==3:
                    n = re.findall(r'[А-я]+', i)
                    if n: print('Жанр:',', '.join(n))
                if strings==4:
                    n = re.findall(r'[А-я]+', i)
                    if n:
                        k = n[1:]
                        print ('Режиссер:', ' '.join(k))
                if strings==5:
                    n = re.findall(r'[А-я]+', i)
                    if n: print('Страна:', n[0])

                if strings>0:
                    strings-=1
                        
                    

            if 'data-name' in i:
                a=((re.split(r'"', i))[1])
                if not a.istitle() and not a.isupper():
                    print('Жанр:', a)
                else:
                    print('Страна:', a)
                print('------------------')
                #new = True

    new = False

    for k in f:
        if not '–' in i and not '…' in i and not '«' in i and not '»' in i and not '—' in i and not 'Ў' in i:#for Win
            if new:
                new = False
                print ((re.split(r'"', i))[1])
            if 'data-name' in k:
                print (k)
                #((re.split(r'"', i))[1])
                new = True
                    
