# get-book-info

This is a small side project. The objective is to get the basic information of the book based on the given ISBN. Specifically, a web crawler based on `BeautifulSoup` is used to get the book information from the item page of [TAAZE.com ](https://www.taaze.tw/index.html), a well-known booksteller in Taiwan.

## Files

- `./requirements.txt`: text file listing required packages and versions.

- `./tutorial.ipynb`: a step-by-step tutorial by demonstrating for one ISBN.

- `./get_book_info.py` defines the end-to-end function of collecting the book info. It can also be directly executed.

- `./examples/` contains inputs and outputs of examples in `./tutorial.ipynb` and running `get_book_info.py`.

## Usage

### Clone this repo and install required packages

```bash
git clone https://github.com/jayenliao/get-book-info.git
cd get-book-info
pip3 install -r requirements.txt
```

### Approaches

#### 1. Follow cells and instructions in `tutorial.ipynb` to view the process for on ISBN

#### 2. For more than one ISBN, directly execute `get_book_info.py` or use function `get_book_info()` defined in `get_book_info.py`

```bash
python3 get_book_info.py
```

Follow the instructions to enter inputs.

<details>
<summary>Example 1: direcly enter ISBN(s)</summary>

```text
How do you want to import ISBN(s)? (a) directly enter / (b) give the path to a file: a
Please enter one or more ISBNs (please separate them with spaces): 9786267149485 9786263299443 9789572049297 9786263185814 9786263244887 9789865918255
Do you want to print out all results? (y/n): y

{'書名': '去日本自助旅行！給超新手的旅遊密技全圖解：交通攻略X食宿玩買X旅程規劃，有問必答萬用QA 暢銷最新版', '作者': '超級旅行貓', '出版社': '創意市集', '出版日期': '2023-01-07', 'ISBN/ISSN': '9786267149485', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '272頁', '開數': '16K', '商品尺寸': '長：230mm \\ 寬：170mm \\ 高：15mm', '類別': '中文書>旅遊>東北亞'}

{'書名': '慢遊法國：美景、藝術、建築、歷史的深度體驗，歐洲線領隊從自助到跟團的隨身導覽攻略', '作者': '魏宏展', '出版社': '台灣東販股份有限公司', '出版日期': '2023-08-28', 'ISBN/ISSN': '9786263299443', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '280頁', '商品尺寸': '長：230mm \\ 寬：170mm \\ 高：15mm', '類別': '中文書>旅遊>歐洲'}

{'書名': 'Word、Excel、PowerPoint 強效精攻500招 ', '作者': 'PCuSER研究室', '出版社': 'PCuSER電腦人文化', '出版日期': '2023-03-04', 'ISBN/ISSN': '9789572049297', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '136頁', '開數': '8K', '商品尺寸': '長：280mm \\ 寬：210mm \\ 高：15mm', '類別': '中文書>電腦>應用軟體'}

{'書名': '都問AI吧！ChatGPT上手的第一本書', '作者': '維圖歐索', '出版社': '商周出版', '出版日期': '2023-03-11', 'ISBN/ISSN': '9786263185814', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '176頁', '開數': '16K', '商品尺寸': '長：210mm \\ 寬：148mm \\ 高：15mm', '類別': '中文書>電腦>應用軟體'}

{'書名': '用Canva設計超快超質感：平面、網頁、電子書、簡報、影片製作與AI繪圖最速技', '作者': '鄧君如、文淵閣工作室', '出版社': '碁峰資訊', '出版日期': '2023-04-27', 'ISBN/ISSN': '9786263244887', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '336頁', '開數': '18', '類別': '中文書>電腦>應用軟體'}

{'書名': '國家地理終極旅遊：一生必遊的500祕境之旅', '作者': '國家地理學會叢書部', '譯者': '方淑惠、余佳玲、許妍飛', '出版社': '大石文化', '出版日期': '2013-07-16', 'ISBN/ISSN': '9789865918255', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '320頁', '商品尺寸': '長：210mm \\ 寬：157mm類別：中文書'}

The final outputs are saved as ./examples/results_6books_20240228-130631.csv
```
</details>

<details>
<summary>Example 2: import ISBNs through reading a csv or txt file</summary>

```text
How do you want to import ISBN(s)? (a) directly enter / (b) give the path to a file: b
Please enter the path to a file with ISBNs: examples/isbn_list.txt
Do you want to print out all results? (y/n): y

{'書名': '去日本自助旅行！給超新手的旅遊密技全圖解：交通攻略X食宿玩買X旅程規劃，有問必答萬用QA 暢銷最新版', '作者': '超級旅行貓', '出版社': '創意市集', '出版日期': '2023-01-07', 'ISBN/ISSN': '9786267149485', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '272頁', '開數': '16K', '商品尺寸': '長：230mm \\ 寬：170mm \\ 高：15mm', '類別': '中文書>旅遊>東北亞'}

{'書名': '慢遊法國：美景、藝術、建築、歷史的深度體驗，歐洲線領隊從自助到跟團的隨身導覽攻略', '作者': '魏宏展', '出版社': '台灣東販股份有限公司', '出版日期': '2023-08-28', 'ISBN/ISSN': '9786263299443', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '280頁', '商品尺寸': '長：230mm \\ 寬：170mm \\ 高：15mm', '類別': '中文書>旅遊>歐洲'}

{'書名': 'Word、Excel、PowerPoint 強效精攻500招 ', '作者': 'PCuSER研究室', '出版社': 'PCuSER電腦人文化', '出版日期': '2023-03-04', 'ISBN/ISSN': '9789572049297', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '136頁', '開數': '8K', '商品尺寸': '長：280mm \\ 寬：210mm \\ 高：15mm', '類別': '中文書>電腦>應用軟體'}

{'書名': '都問AI吧！ChatGPT上手的第一本書', '作者': '維圖歐索', '出版社': '商周出版', '出版日期': '2023-03-11', 'ISBN/ISSN': '9786263185814', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '176頁', '開數': '16K', '商品尺寸': '長：210mm \\ 寬：148mm \\ 高：15mm', '類別': '中文書>電腦>應用軟體'}

{'書名': '用Canva設計超快超質感：平面、網頁、電子書、簡報、影片製作與AI繪圖最速技', '作者': '鄧君如、文淵閣工作室', '出版社': '碁峰資訊', '出版日期': '2023-04-27', 'ISBN/ISSN': '9786263244887', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '336頁', '開數': '18', '類別': '中文書>電腦>應用軟體'}

{'書名': '國家地理終極旅遊：一生必遊的500祕境之旅', '作者': '國家地理學會叢書部', '譯者': '方淑惠、余佳玲、許妍飛', '出版社': '大石文化', '出版日期': '2013-07-16', 'ISBN/ISSN': '9789865918255', '語言': '繁體中文', '裝訂方式': '平裝', '頁數': '320頁', '商品尺寸': '長：210mm \\ 寬：157mm類別：中文書'}

The final outputs are saved as ./examples/results_6books_20240228-152745.csv
```

</details>

<details>
<summary>Output files of these two examples, `./examples/results_6books_20240228-130631.csv` and `./examples/results_6books_20240228-152745.csv`, look like:</summary>

|               |  書名                                                  |  作者          |  出版社          |  出版日期        |  ISBN/ISSN      |  語言    |  裝訂方式  |  頁數    |  開數   |  商品尺寸                        |  類別           |  譯者
---------------|------------------------------------------------------|--------------|---------------|--------------|-----------------|--------|--------|--------|-------|------------------------------|---------------|-------------
9786267149485  |  去日本自助旅行！給超新手的旅遊密技全圖解：交通攻略X食宿玩買X旅程規劃，有問必答萬用QA 暢銷最新版  |  超級旅行貓       |  創意市集         |  2023-01-07  |  9786267149485  |  繁體中文  |  平裝    |  272頁  |  16K  |  長：230mm \ 寬：170mm \ 高：15mm  |  中文書>旅遊>東北亞   |
9786263299443  |  慢遊法國：美景、藝術、建築、歷史的深度體驗，歐洲線領隊從自助到跟團的隨身導覽攻略            |  魏宏展         |  台灣東販股份有限公司   |  2023-08-28  |  9786263299443  |  繁體中文  |  平裝    |  280頁  |       |  長：230mm \ 寬：170mm \ 高：15mm  |  中文書>旅遊>歐洲    |
9789572049297  |  Word、Excel、PowerPoint 強效精攻500招                      |  PCuSER研究室   |  PCuSER電腦人文化  |  2023-03-04  |  9789572049297  |  繁體中文  |  平裝    |  136頁  |  8K   |  長：280mm \ 寬：210mm \ 高：15mm  |  中文書>電腦>應用軟體  |
9786263185814  |  都問AI吧！ChatGPT上手的第一本書                                |  維圖歐索        |  商周出版         |  2023-03-11  |  9786263185814  |  繁體中文  |  平裝    |  176頁  |  16K  |  長：210mm \ 寬：148mm \ 高：15mm  |  中文書>電腦>應用軟體  |
9786263244887  |  用Canva設計超快超質感：平面、網頁、電子書、簡報、影片製作與AI繪圖最速技             |  鄧君如、文淵閣工作室  |  碁峰資訊         |  2023-04-27  |  9786263244887  |  繁體中文  |  平裝    |  336頁  |  18   |                              |  中文書>電腦>應用軟體  |
9789865918255  |  國家地理終極旅遊：一生必遊的500祕境之旅                               |  國家地理學會叢書部   |  大石文化         |  2013-07-16  |  9789865918255  |  繁體中文  |  平裝    |  320頁  |       |  長：210mm \ 寬：157mm類別：中文書     |               |  方淑惠、余佳玲、許妍飛
</details>
