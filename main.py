from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as url_r_o

my_url = 'https://rozetka.com.ua/universalnye-mobilnye-batarei/c387969/48980=zaryadka-ot-solnechnoy-energii/'
# open connection, grab the page
uClient = url_r_o(my_url)
page_html = uClient.read()
uClient.close()

# html pars
page_soup = soup(page_html, 'html.parser')

# grab each container
containers = page_soup.findAll('div', {'class': 'goods-tile__inner'})

f_name = 'PB_wth_SB_roz.csv'
f_w = open(f_name, 'w')

headers = 'Item ID, Item Information, Price, Available\n'

f_w.write(headers)

for container in containers:
    avail = container.find('div', {'class': 'goods-tile__availability'}).text.strip()
    if len(avail) < 14:
        containers.remove(container)

    itm_inf = container.a.img['alt'].replace(',', ' ')

    itm_id = container.get('data-goods-id')

    price = container.p.span.text.replace(' ', '')
    f_w.write(itm_id + ';' + itm_inf + ';' + price + ';' + avail + '\n')

f_w.close()
