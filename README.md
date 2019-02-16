# Parsers
some vk/kinopoisk parsers on python:

vkgrp - taking ids from users in group for Dmitry (change params, if u need), using API vk.

kinopoisk - parsing pages in top 500 (?)

parse - parsing particular page, fetching more info. 

u can connect two last scripts)



p.s. may use soup for better results without making new text files, but here is simple ones

pps 
from fake_useragent import UserAgent
ru = UserAgent()
ru.opera
headers = {'user-agent':f'{ru.opera}'}
r = requests.get(url, auth('name', 'pass'), headers = headers)
r.text
