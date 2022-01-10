import requests

lapa = requests.get("http://vilanuvidusskola.blogspot.com/")
print(lapa)
#print(lapa.content)

soup = BeautifulSoup(lapa.content,'html.parser')
print(soup.prettyfy)