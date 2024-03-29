html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>İlk web sayfam</title>
</head>
<body>

 <h1 id="header">
        Python Kursu
 </h1>

 <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">

    <a href="http://example1.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example2.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example3.com/tillie" class="sister" id="link3">Tillie</a>;

</body>
</html>





"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body


result = soup.title.string
result = soup.h1.string


result = soup.find_all('h2')
result = soup.find_all('h2')[0]
result = soup.find_all('h2')[1]

result = soup.div
result = soup.find_all('div')
result = soup.find_all('div')[0]
result = soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren()
result = soup.div.findNextSibling()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

result = soup.find_all('a')

for link in result:
    print(link.get('href'))

