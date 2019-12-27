import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as url_r_o

# make folder
os.makedirs('w_sample')
os.chdir('./w_sample')


main_URL = "https://www.mediawiki.org/wiki/API:Main_page"
beg = 'https://www.mediawiki.org/'


uClient = url_r_o(main_URL)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

media_action_list = page_soup.find('td', {'class': ""})
pre_url_list = media_action_list.findAll('a')

for part in pre_url_list:
    target = part.get('href')
    if target[6:9] != 'API':
        continue
    each_url = beg + target
    pClient = url_r_o(each_url)
    p_thtml = pClient.read()
    pClient.close()
    p_soup = soup(p_thtml, 'html.parser')
    sample_code = p_soup.body.find('div', {'class': 'mw-gadget-tabbedwindow'})
    if sample_code:
        inside = sample_code.pre
        f_name = inside.findAll('span')[3].text.strip()
        f_wr = open(f_name, 'w')
        f_wr.write(inside.text)
        f_wr.close()


