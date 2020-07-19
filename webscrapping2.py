import requests

from bs4 import BeautifulSoup

url="http://www.newsonair.com/"


resp=requests.get(url)
page=BeautifulSoup(resp.text,'html.parser')


Head_Lines=page.findAll('a', {'class': 'top-links'})


print('The Top Headlines are:')

print(" ")


for Head_Line in Head_Lines:
 
            print(Head_Line.text)
 
            print(" ")