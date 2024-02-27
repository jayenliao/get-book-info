'''
get_book_info.py

This is a python code for getting basic info of a book.
Given ISBN of a book, the code would get basic info of the book from TAZZE.com.

Created by Jay Liao (jay.chiehen[at]gmail.com) on 21 Oct 2019
Upated on 27 Feb 2024
'''

# import the packages
import re
import time, datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_book_info(ISBN:int, verbose:bool=False):
    tStart = time.time()

    # Visit the searching page of the given ISBN
    url_root1 = 'https://www.taaze.tw/rwd_searchResult.html?keyType%5B%5D=0&keyword%5B%5D='
    url_root2 = '&prodKind=0&prodCatId=0&catId=0&saleDiscStart=0&saleDiscEnd=0&salePriceStart=&salePriceEnd=&publishDateStart=&publishDateEnd=&prodRank=0&addMarkFlg=0&force=0&catFocus=11&orgFocus=A&layout=A&nowPage=1&sort='
    r = requests.get(f'{url_root1}{ISBN}{url_root2}')
    soup = bs(r.text, 'html.parser')

    # Find the url of the target goods page
    d_product_id = {}
    a_tags = soup.find_all('a')
    pattern = f'https://www.taaze.tw/products/'

    for tag in a_tags:
        url = tag.get('href')
        if url is not None and pattern in url:
            id = url.split(pattern)[-1].split('.html')[0]
            if id not in d_product_id.keys():
                d_product_id[id] = 1
            else:
                d_product_id[id] += 1

    for k, v in d_product_id.items():
        if v == 1:
            product_id = k
            target_url = f'{pattern}{product_id}.html'
            break

    if verbose:
        print('Target URL:', target_url)

    # Visit the main page of the target book
    r2 = requests.get(target_url)
    soup2 = bs(r2.text, 'html.parser')

    # Obtain all the texts on the visited page
    all_tags = soup2.find_all(text=True)
    lst_all_tags = []
    for tag in all_tags:
        lst_all_tags.append(tag)

    # Remove useless texts
    for i in range(lst_all_tags.count('\n')):
        lst_all_tags.remove('\n')

    # Obtain the book title and info
    d_info = {
        '書名': lst_all_tags[1].replace('- TAAZE 讀冊生活', '')
    }
    idx_info = lst_all_tags.index('商品資料')
    idx_end = lst_all_tags.index('類別有誤？')
    i = idx_info+1
    while i < idx_end:
        if '：' in lst_all_tags[i]:
            k = lst_all_tags[i].replace('：', '')
            if lst_all_tags[i] == '類別：':
                #idx_genre = lst_all_tags.index('類別：')
                v = ''.join(lst_all_tags[i+1:idx_end])
            elif lst_all_tags[i] == '商品尺寸：':
                v = ''.join(lst_all_tags[i+1:i+6])
                i += 5
            else:
                v = lst_all_tags[i+1]
            d_info[k] = v
        i += 1

    if verbose:
        print('\nTime cost: %10.6f s' % (time.time() - tStart))

    return d_info

if __name__ == '__main__':
    mode = ''
    while mode != 'a' and mode != 'b':
        mode = input('How do you want to import ISBN(s)? (a) directly enter / (b) give the path to a file: ')
        mode = mode.lower()
        if mode != 'a' and mode != 'b':
            print('Please enter either a or b.')

    if mode == 'a':
        lst_ISBN = input('Please enter one or more ISBNs (please separate them with spaces): ')
    elif mode == 'b':
        fn = input('Please enter the path to a file with ISBNs: ')
        if fn.endswith('.csv'):
            lst_ISBN = pd.read_csv(fn).iloc[0]
        elif fn.endswith('.txt'):
            with open(fn, 'f') as f:
                lst_ISBN = f.readlines()
    lst_ISBN = [int(x) for x in lst_ISBN.split(' ')]

    print_out = ''
    while print_out not in ['y', 'n']:
        print_out = input('Do you want to print out all results? (y/n): ')
        print_out = print_out.lower()

    saved_fn = ''
    while saved_fn != '' and not saved_fn.endswith('.csv'):
        saved_fn = input('Enter a csv file path to save the results as a file. Press enter to use a default path: ')
        if saved_fn != '' and not saved_fn.endswith('.csv'):
            print('Only a csv file path is allowed.')

    if saved_fn == '':
        n_books = len(lst_ISBN)
        dt = datetime.datetime.now()
        dt = dt.strftime('%Y%m%d-%H%M%S')
        saved_fn = f'./examples/results_{n_books}books_{dt}.csv'
    print()


    lst_results = []
    for ISBN in lst_ISBN:
        results = get_book_info(ISBN)
        if print_out == 'y':
            print(results, '\n')
        lst_results.append(results)

    lst_df = [
        pd.DataFrame(results, index=[ISBN]) for results, ISBN in zip(lst_results, lst_ISBN)
    ]
    df_concat = pd.concat(lst_df)
    df_concat.to_csv(saved_fn)
    print('The final outputs are saved as', saved_fn)
