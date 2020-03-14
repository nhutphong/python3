from bs4 import BeautifulSoup
import requests

# with open("/root/code/python/learn/html/bongda.html") as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

html_file = requests.get('https://tinhte.vn/')
soup = BeautifulSoup(html_file.content,'lxml')

get_header = soup.find('header')
print(type(get_header))