'''
get_book_info.py

This is a python code for getting basic info of a book.
Given ISBN of a book, the code would get basic info of the book from TAZZE.com.

Coded by Jay Chiehen Liao, email: jay.chiehen@gmail.com
Date: 2019.10.21
'''

# import the packages
import re
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_book_info(ISBN):
    
    # import the packages
    import re
    import time
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    
    tStart = time.time()
    
    # Visit the searching page of the given ISBN
    url_root = 'https://www.taaze.tw/rwd_searchResult.html?keyType%5B%5D=0&keyword%5B%5D='
    r = requests.get(url_root + str(ISBN))
    soup = bs(r.text, 'html.parser')
    
    # Find the url of the target goods page
    lst_tags_str, lst_tags_url = [], []
    a_tags = soup.find_all('a')
    for tag in a_tags:
        lst_tags_str.append(tag.string)
        lst_tags_url.append(tag.get('href'))
    target_srt = lst_tags_str[lst_tags_str.index('我不滿意搜尋結果的商品順序')-1]
    target_url = lst_tags_url[lst_tags_str.index('我不滿意搜尋結果的商品順序')-1]
    
    if 'https://' in target_url:   
        print(target_srt)
        print(target_url)

        # Visit the goods page of the givien ISBN
        target_url2 = target_url[target_url.index('purl=')+5:target_url.index('.html')+5]
        print(target_url2)
        r_target2 = requests.get(target_url2)
        soup_target2 = bs(r_target2.text, 'html.parser')

        # Obtain all the texts on the visited page
        all_tags = soup_target2.find_all(text=True)
        lst_all_tags = []
        for tag in all_tags:
            lst_all_tags.append(tag)

        # Remove useless texts
        for i in range(lst_all_tags.count('\n')):
            lst_all_tags.remove('\n')

        # Obtain the book info and return it out
        if '商品資料' in lst_all_tags:
            idx = lst_all_tags.index('商品資料')
            book_info = target_srt + '\', ' + str(lst_all_tags[idx:idx+25])[1:]
            return book_info
        else:
            return 'NA\', \''*25
    
    else:
        return 'NA\', \''*25
    #print('\nTime cost: %10.6f s' % (time.time() - tStart))