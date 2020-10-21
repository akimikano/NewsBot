import requests
from bs4 import BeautifulSoup

source = requests.get('https://kicb.net/welcome/').text
soup = BeautifulSoup(source, 'lxml')

buying = []
selling = []

a = soup.find('div', class_='con')
b = a.find_all('div', class_='cur_line')
b.remove(b[0])
for i in b:
    buying1 = i.find('div', class_='data2')
    buying2 = buying1.span.text
    buying.append(buying2)

    selling1 = i.find('div', class_='data3')
    selling2 = selling1.span.text
    selling.append(selling2)

print(buying)
print(selling)