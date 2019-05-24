#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import re
import requests
import os

if not os.path.exists('qbittorrent_donwnload_py'):
    os.mkdir('qbittorrent_donwnload_py')
DirPath = os.path.join(os.getcwd(), 'qbittorrent_donwnload_py')
UrlM = r'https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins'
pattern = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
result = pattern.findall((requests.get(UrlM)).text)
urs = [x for x in result if x[-3::] == '.py']
for i, ur in enumerate(urs):
    print('-'*60+'\n' + 'NO. '+ str(i+1) +'：' + ur)
    firename = os.path.join(DirPath, ur[-(len(ur)-ur.rfind(r'/')-1)::])
    # wtxt=r'# -*- coding: utf-8 -*-\n'+requests.get(ur).text
    wtxt = requests.get(ur).text
    with open(firename, mode='w+', encoding='utf-8') as w:
        w.write(wtxt)
        w.flush()
        print('NO. '+ str(i+1) +'：' + firename)
print('ok！')
